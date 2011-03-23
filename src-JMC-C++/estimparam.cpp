/*
 * estimparam.cpp
 *
 *  Created on: 9 march 2011
 *      Author: cornuet
 */
#ifndef HEADER
#include "header.cpp"
#define HEADER
#endif

#ifndef VECTOR
#include <vector>
#define VECTOR
#endif

#ifndef MATRICES
#include "matrices.cpp"
#define MATRICES
#endif

#ifndef MESUTILS
#include "mesutils.cpp"
#define MESUTILS
#endif

#ifndef GLOBALH
#include "global.h"
#define GLOBALH
#endif

using namespace std;

#define c 1.5707963267948966192313216916398
#define co 2.506628274631000502415765284811   //sqrt(pi)
#define coefbw 1.8                            //coefficient multiplicateur de la bandwidth pour le calcul de la densité 


/**
* définition de la densité d'un paramètre
*/
struct pardensC {
    double *x,*priord,*postd;
    double xmin,xmax,xdelta;
    int ncl;
};

struct parstatC {
    double moy,med,mod,q025,q050,q250,q750,q950,q975;
};

//variables globales du module;
pardensC *pardens;
double *var_stat, *parmin, *parmax, *diff;
double **beta, **phistar,**simpar;
int nparamcom,nparcompo,**numpar,numtransf,npar,npar0;
double borne=10.0,xborne;
bool composite,original;
string entete;
int nsimpar=100000;
string *nomparam;
parstatC *parstat;

    
/** 
* compte les paramètres communs aux scénarios choisis (nparamcom), le nombre de paramètres composites
* rempli le tableau numpar des numéros de paramètres communs par scénario
*/
    void det_numpar() {
        vector <string>  parname;
        int ii;
        bool commun,trouve;
        npar=0;npar0=0;
        numpar = new int*[rt.nscenchoisi]; 
        if (rt.nscenchoisi==1) {
            numpar[0] = new int[rt.nparam[rt.scenchoisi[0]-1]];
            for (int i=0;i<rt.nparam[rt.scenchoisi[0]-1];i++) numpar[0][i]=i;
            for (int i=0;i<header.scenario[rt.scenchoisi[0]-1].nparam;i++) {
                if (not header.scenario[rt.scenchoisi[0]-1].histparam[i].prior.constant){
                    npar++;
                    parname.push_back(header.scenario[rt.scenchoisi[0]-1].histparam[i].name);
                    if (header.scenario[rt.scenchoisi[0]-1].histparam[i].category<2) npar0++;
                }
            }
            cout << "noms des parametres communs : ";
            for (int i=0;i<npar;i++) cout<<parname[i]<<"   ";
            cout <<"\n";
        } else {
            for (int i=0;i<header.scenario[rt.scenchoisi[0]-1].nparam;i++) {
                commun=true;
                for (int j=1;j<rt.nscenchoisi;j++) {
                    trouve=false;
                    for (int k=0;k<header.scenario[rt.scenchoisi[j]-1].nparam;k++) {
                        trouve=(header.scenario[rt.scenchoisi[0]-1].histparam[i].name.compare(header.scenario[rt.scenchoisi[j]-1].histparam[k].name)==0);
                        if (trouve) break;
                    }
                    commun=trouve;
                    if (not commun) break;
                }
                if (commun) {
                    if (not header.scenario[rt.scenchoisi[0]-1].histparam[i].prior.constant){
                        npar++;
                        parname.push_back(header.scenario[rt.scenchoisi[0]-1].histparam[i].name);
                        if (header.scenario[rt.scenchoisi[0]-1].histparam[i].category<2) npar0++;
                    }
                }
            }
            cout << "noms des parametres communs : ";
            for (int i=0;i<npar;i++) cout<<parname[i]<<"   ";
            cout <<"\n";
        } 
        //cout<<"npar0="<<npar0<<"   npar="<<npar<<"   nombre de groupes="<<header.ngroupes<<"\n";
        if (composite) nparcompo=npar0*header.ngroupes; else nparcompo=0;
        cout<<"nombre de parametres composites : "<<nparcompo<<"\n";
        nparamcom = npar+rt.nparam[rt.scenchoisi[0]-1]-header.scenario[rt.scenchoisi[0]-1].nparam;
        cout<<"nombre de parametres communs : "<<nparamcom<<"\n";
        for (int j=0;j<rt.nscenchoisi;j++) {
            numpar[j] = new int[nparamcom];
            ii=0;
            for (int i=0;i<npar;i++) {
                for (int k=0;k<header.scenario[rt.scenchoisi[j]-1].nparam;k++) {
                    if (header.scenario[rt.scenchoisi[j]-1].histparam[k].name.compare(parname[i])==0) {numpar[j][ii]=k;ii++;}  
                }
            }
            for (int k=header.scenario[rt.scenchoisi[j]-1].nparam;k<rt.nparam[rt.scenchoisi[j]-1];k++) {numpar[j][ii]=k;ii++;}
            for (int kk=0;kk<npar+rt.nparam[rt.scenchoisi[j]-1]-header.scenario[rt.scenchoisi[j]-1].nparam;kk++) {
              cout <<numpar[j][kk]<<"  ";
              if (kk<npar) cout<<"("<<header.scenario[rt.scenchoisi[j]-1].histparam[numpar[j][kk]].name<<")  ";
            }
            cout<<"\n";
        }
        
    }

/** 
* recalcule les valeurs de paramètres en fonction de la transformation choisie 
*/
    void recalparam(int n) {
        double coefmarge=0.001,marge;
        int jj,k,kk;
        alpsimrat = new double*[n];
        for(int i=0;i<n;i++) alpsimrat[i] = new double[nparamcom];
        switch (numtransf) {
        
          case 1 :  //no transform
                   for (int i=0;i<n;i++) {
                       for (int j=0;j<nparamcom;j++) {
                           k=0;while(rt.enrsel[i].numscen!=rt.scenchoisi[k])k++;
                           //k = rt.enrsel[i].numscen-1;
                           alpsimrat[i][j] = rt.enrsel[i].param[numpar[k][j]];
                       }    
                   }
                   break;
          case 2 : // log transform
                   for (int i=0;i<n;i++) {
                       for (int j=0;j<nparamcom;j++) {
                           k=0;while(rt.enrsel[i].numscen!=rt.scenchoisi[k])k++;
                           //k = rt.enrsel[i].numscen-1;
                           if (rt.enrsel[i].param[numpar[k][j]]<=0.00000000001) rt.enrsel[i].param[numpar[k][j]]=1E-11;
                           alpsimrat[i][j] = log(rt.enrsel[i].param[numpar[k][j]]);
                       }    
                   }
                   break;
          case 3 : //logit transform
                   //cout<<"borne="<<borne<<"\n";
                   parmin = new double[nparamcom]; parmax = new double[nparamcom]; diff = new double[nparamcom];
                   if (borne<0.0000000001) {
                       xborne=1E100;
                       for (int j=0;j<nparamcom;j++) {parmin[j]=1E100;parmax[j]=-1E100;}
                       for (int i=0;i<n;i++) {
                            for (int j=0;j<nparamcom;j++) {
                                k=0;while(rt.enrsel[i].numscen!=rt.scenchoisi[k])k++;
                                //k = rt.enrsel[i].numscen-1;
                                if (rt.enrsel[i].param[numpar[k][j]]<parmin[j]) parmin[j]=rt.enrsel[i].param[numpar[k][j]];
                                if (rt.enrsel[i].param[numpar[k][j]]>parmax[j]) parmax[j]=rt.enrsel[i].param[numpar[k][j]];
                           }
                       }
                       for (int j=0;j<nparamcom;j++) {
                           diff[j]=parmax[j]-parmin[j];
                           marge=coefmarge*diff[j];
                           parmin[j] -=marge;
                           parmax[j] +=marge;
                           diff[j]=parmax[j]-parmin[j];
                       }
                   } else{
                       xborne=borne;
                       //k=0;while(rt.enrsel[i].numscen!=rt.scenchoisi[k]) k++;
                       //k=rt.scenchoisi[0]-1;
                       //cout<<"k="<<k<<"\n";
                       for (int j=0;j<nparamcom-header.nparamut;j++) {
                           if (header.scenario[k].histparam[numpar[k][j]].category<2) {
                               parmin[j] = header.scenario[k].histparam[numpar[0][j]].prior.mini-0.5;
                               parmax[j] = header.scenario[k].histparam[numpar[0][j]].prior.maxi+0.5;
                           } else {
                               parmin[j] = header.scenario[k].histparam[numpar[0][j]].prior.mini-0.0005;
                               parmax[j] = header.scenario[k].histparam[numpar[0][j]].prior.maxi+0.0005;
                           }
                           diff[j]=parmax[j]-parmin[j];
                           //cout<<header.scenario[k].histparam[numpar[k][j]].name<<"   ";
                           //cout<<"parmin = "<<parmin[j]<<"   parmax="<<parmax[j]<<"\n";
                       }
                       for (int j=nparamcom-header.nparamut;j<nparamcom;j++) {
                               jj=j-(nparamcom-header.nparamut);
                               //cout<<"jj="<<jj<<"\n";
                               parmin[j]=0.95*header.mutparam[jj].prior.mini;
                               parmax[j]=1.05*header.mutparam[jj].prior.maxi;
                               //cout<<header.mutparam[jj].category<<"   ";
                               //cout<<"parmin = "<<parmin[j]<<"   parmax="<<parmax[j]<<"\n";
                               diff[j]=parmax[j]-parmin[j];
                       }
                   }
                   //cout <<"fin du calcul de parmin/parmax rt.scenchoisi[0] = "<<rt.scenchoisi[0]<<"\n";
                   //for (int i=0;i<10;i++) cout <<rt.enrsel[i].numscen<<"\n";
                   for (int i=0;i<n;i++) {
                       for (int j=0;j<nparamcom;j++) {
                           k=0;while(rt.enrsel[i].numscen!=rt.scenchoisi[k])k++;
                           //k = rt.enrsel[i].numscen-1;
                           //cout <<"k="<<k<<"   j="<<j<<"\n";
                           //cout<<numpar[k][j]<<"\n";
                           if (rt.enrsel[i].param[numpar[k][j]]<=parmin[j]) alpsimrat[i][j] = -xborne;
                           else if (rt.enrsel[i].param[numpar[k][j]]>=parmax[j]) alpsimrat[i][j] = xborne;
                           else alpsimrat[i][j] =log((rt.enrsel[i].param[numpar[k][j]]-parmin[j])/(parmax[j]-rt.enrsel[i].param[numpar[k][j]]));
                       }
                   }
                   break;
          case 4 : //log(tg) transform
                   parmin = new double[nparamcom]; parmax = new double[nparamcom]; diff = new double[nparamcom];
                   if (borne<0.0000000001) {
                       xborne=1E100;
                       for (int j=0;j<nparamcom;j++) {parmin[j]=1E100;parmax[j]=-1E100;}
                       for (int i=0;i<n;i++) {
                            for (int j=0;j<nparamcom;j++) {
                                k=0;while(rt.enrsel[i].numscen!=rt.scenchoisi[k])k++;
                                //k = rt.enrsel[i].numscen-1;
                                if (rt.enrsel[i].param[numpar[k][j]]<parmin[j]) parmin[j]=rt.enrsel[i].param[numpar[k][j]];
                                if (rt.enrsel[i].param[numpar[k][j]]>parmax[j]) parmax[j]=rt.enrsel[i].param[numpar[k][j]];
                           }
                       }
                       for (int j=0;j<nparamcom;j++) {
                           diff[j]=parmax[j]-parmin[j];
                           marge=coefmarge*diff[j];
                           parmin[j] -=marge;
                           parmax[j] +=marge;
                           diff[j]=parmax[j]-parmin[j];
                       }
                   } else{
                       xborne=borne;
                       //k=0;while(rt.enrsel[i].numscen!=rt.scenchoisi[k])k++;
                       //k=rt.scenchoisi[0]-1;
                       for (int j=0;j<nparamcom-header.nparamut;j++) {
                           if (header.scenario[k].histparam[numpar[k][j]].category<2) {
                               parmin[j] = header.scenario[k].histparam[numpar[0][j]].prior.mini-0.5;
                               parmax[j] = header.scenario[k].histparam[numpar[0][j]].prior.maxi+0.5;
                           } else {
                               parmin[j] = header.scenario[k].histparam[numpar[0][j]].prior.mini-0.0005;
                               parmax[j] = header.scenario[k].histparam[numpar[0][j]].prior.maxi+0.0005;
                           }
                           diff[j]=parmax[j]-parmin[j];
                           //cout<<header.scenario[k].histparam[numpar[k][j]].name<<"   ";
                           //cout<<"parmin = "<<parmin[j]<<"   parmax="<<parmax[j]<<"\n";
                       }
                       for (int j=nparamcom-header.nparamut;j<nparamcom;j++) {
                               jj=j-(nparamcom-header.nparamut);
                               cout<<"jj="<<jj<<"\n";
                               parmin[j]=0.95*header.mutparam[jj].prior.mini;
                               parmax[j]=1.05*header.mutparam[jj].prior.maxi;
                               cout<<header.mutparam[jj].category<<"   ";
                               //cout<<"parmin = "<<parmin[j]<<"   parmax="<<parmax[j]<<"\n";
                               //diff[j]=parmax[j]-parmin[j];
                       }
                   }
                   //cout <<"fin du calcul de parmin/parmax\n";
                   for (int i=0;i<n;i++) {
                       for (int j=0;j<nparamcom;j++) {
                           k=0;while(rt.enrsel[i].numscen!=rt.scenchoisi[k])k++;
                           //k = rt.enrsel[i].numscen-1;
                           if (rt.enrsel[i].param[numpar[k][j]]<=parmin[j]) alpsimrat[i][j] = -xborne;
                           else if (rt.enrsel[i].param[numpar[k][j]]>=parmax[j]) alpsimrat[i][j] = xborne;
                           else alpsimrat[i][j] =log(tan((rt.enrsel[i].param[numpar[k][j]]-parmin[j])*c/diff[j]));
                       }
                   }
                   break;
        }
    }   

/** 
* effectue le remplissage de la matrice matX0, du vecteur des poids vecW et 
* de la matrice des paramètres parsim (éventuellement transformés)
*/
    void rempli_mat(int n,double* stat_obs) {
        int icc;
        double delta,som,x,*var_statsel,nn;
        double *sx,*sx2,*mo;
        nn=(double)n;
        delta = rt.enrsel[n-1].dist;
        //cout<<"delta="<<delta<<"\n";
        sx  = new double[rt.nstat];
        sx2 = new double[rt.nstat];
        mo  = new double[rt.nstat];
        var_statsel = new double[rt.nstat];
        for (int i=0;i<rt.nstat;i++){sx[i]=0.0;sx2[i]=0.0;mo[i]=0.0;}
        for (int i=0;i<n;i++){
            for (int j=0;j<rt.nstat;j++) {
                x = rt.enrsel[i].stat[j];
                sx[j] +=x;
                sx2[j] +=x*x;
            }
        }
        nstatOKsel=0;
        for (int j=0;j<rt.nstat;j++) {
            var_statsel[j]=(sx2[j]-sx[j]/nn*sx[j])/(nn-1.0);
            if (var_statsel[j]>0.0) nstatOKsel++;
            mo[j] = sx[j]/nn;
        }
        matX0 = new double*[n];
        for (int i=0;i<n;i++)matX0[i]=new double[nstatOKsel];
        vecW = new double[n];
        //cout <<"hello\n";  
        som=0.0;
        for (int i=0;i<n;i++) {
            icc=-1;
            for (int j=0;j<rt.nstat;j++) {
                if (var_statsel[j]>0.0) {
                    icc++;
                    matX0[i][icc]=(rt.enrsel[i].stat[j]-stat_obs[j])/sqrt(var_statsel[j]);
                }
            }
            x=rt.enrsel[i].dist/delta;
            vecW[i]=(1.5/delta)*(1.0-x*x);
            som = som + vecW[i];
        }

        for (int i=0;i<n;i++) vecW[i]/=som;
        //for (int i=0;i<10;i++) cout<<vecW[i]<<"  ";
        //cout<<"\n";
        parsim = new double*[n];
        for (int i=0;i<n;i++) parsim[i] = new double[nparamcom];
        for (int i=0;i<n;i++) {
            for (int j=0;j<nparamcom;j++)parsim[i][j]=alpsimrat[i][j];
        }
    }

/** 
* effectue la régression locale à partir de la matrice matX0 et le vecteur des poids vecW
*/
    void local_regression(int n, bool multithread) {
        double **matX,**matXT,**matA,**matB,**matAA,**matC;
        
        matA = new double*[nstatOKsel+1];
        for (int j=0;j<nstatOKsel+1;j++) matA[j] = new double[n];
        matX = new double*[n];
        for (int i=0;i<n;i++) {
            matX[i] = new double[nstatOKsel+1];
            matX[i][0] = 1.0;
            for (int j=1;j<nstatOKsel+1;j++) matX[i][j] = matX0[i][j-1];
        }
        //ecrimat("matX0",10,nstatOKsel,matX0);
        //ecrimat("matX",10,nstatOKsel+1,matX);
        matXT = transpose(n,nstatOKsel+1,matX);
        for (int i=0;i<n;i++) {
            for (int j=0;j<nstatOKsel+1;j++) matA[j][i] = matXT[j][i]*vecW[i];
        }
        //ecrimat("matA",nstatOKsel+1,nstatOKsel+1,matA);
        matAA = prodM(nstatOKsel+1,n,nstatOKsel+1,matA,matX);
        //ecrimat("matAA",nstatOKsel+1,nstatOKsel+1,matAA);
        matB = inverse(nstatOKsel+1,matAA,multithread);
        matC = prodM(nstatOKsel+1,nstatOKsel+1,n,matB,matA);
        beta = prodM(nstatOKsel+1,n,nparamcom,matC,parsim);
        //ecrimat("beta",nstatOKsel+1,nparamcom,beta);
        libereM(nstatOKsel+1,matA);
        libereM(n,matX);
        libereM(nstatOKsel+1,matB);
        libereM(nstatOKsel+1,matAA);
        libereM(nstatOKsel+1,matC);
    }

/** 
* calcule les phistars pour les paramètres originaux et composites
*/
    void calphistar(int n){
        //cout<<"debut de calphistar\n";
        int k,kk,qq;
        double pmut;
        phistar = new double*[n];
        for (int i=0;i<n;i++) phistar[i] = new double[nparamcom+nparcompo];
        for (int i=0;i<n;i++) {
            for (int j=0;j<nparamcom;j++) {
                phistar[i][j] = alpsimrat[i][j];
                //if (i==0) cout<< phistar[i][j]<<"   ";
                for (int k=0;k<nstatOKsel;k++) phistar[i][j] -= matX0[i][k]*beta[k+1][j];
                //if(i==0) cout<< phistar[i][j]<<"   ";
                switch(numtransf) {
                  case 1 : break;
                  case 2 : if (phistar[i][j]<100.0) phistar[i][j] = exp(phistar[i][j]); else phistar[i][j]=exp(100.0);
                           break; 
                  case 3 : if (phistar[i][j]<=-xborne) phistar[i][j] = parmin[j];
                           else if (phistar[i][j]>=xborne) phistar[i][j] = parmax[j];
                           else phistar[i][j] = (exp(phistar[i][j])*parmax[j]+parmin[j])/(1.0+exp(phistar[i][j]));
                           //if(i==0) cout<< phistar[i][j]<<"\n";
                           break;
                  case 4 : if (phistar[i][j]<=-xborne) phistar[i][j] = parmin[j];
                           else if (phistar[i][j]>=xborne) phistar[i][j] = parmax[j];
                           else phistar[i][j] =parmin[j] +(diff[j]/c*atan(exp(phistar[i][j])));
                           break;
                }
            }
        }
        if (nparcompo>0) {
            k=0;
            for (int gr=1;gr<header.ngroupes+1;gr++) {
                if (header.groupe[gr].type==0) {
                    if (header.groupe[gr].priormutmoy.constant) {
                        if (header.groupe[gr].priorsnimoy.constant) {
                            pmut = header.groupe[gr].mutmoy+header.groupe[gr].snimoy;
                            for (int j=0;j<npar;j++) {
                                if (header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].category<2){
                                    for (int i=0;i<n;i++) {
                                          phistar[i][nparamcom+k] = pmut*phistar[i][j];
                                    }    
                                    k++;
                                }
                            }
                        } else {
                            kk=0;while (not ((header.mutparam[kk].groupe == gr)and(header.mutparam[kk].category ==2))) kk++;
                            for (int j=0;j<npar;j++) {
                                if (header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].category<2){
                                    for (int i=0;i<n;i++) {
                                        pmut = header.groupe[gr].mutmoy+phistar[i][npar+kk];
                                        phistar[i][nparamcom+k] = pmut*phistar[i][j];
                                    }    
                                    k++;
                                }
                            }
                        }
                    } else {
                        if (header.groupe[gr].priorsnimoy.constant) {
                            kk=0;while (not ((header.mutparam[kk].groupe == gr)and(header.mutparam[kk].category ==0))) kk++;
                            for (int j=0;j<npar;j++) {
                                if (header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].category<2){
                                    for (int i=0;i<n;i++) {
                                        pmut =phistar[i][npar+kk] +header.groupe[gr].snimoy;
                                        phistar[i][nparamcom+k] = pmut*phistar[i][j];
                                    }    
                                    k++;
                                }
                            }
                        } else {
                            kk=0;while (not ((header.mutparam[kk].groupe == gr)and(header.mutparam[kk].category ==0))) kk++;
                            qq=0;while (not ((header.mutparam[qq].groupe == gr)and(header.mutparam[qq].category ==2))) qq++;
                            for (int j=0;j<npar;j++) {
                                if (header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].category<2){
                                    for (int i=0;i<n;i++) {
                                        pmut =phistar[i][npar+kk]+phistar[i][npar+qq];
                                        phistar[i][nparamcom+k] = pmut*phistar[i][j];
                                    }    
                                    k++;
                                }
                            }
                        }
                    }
                } 
                if (header.groupe[gr].type==1) {    
                    if (header.groupe[gr].priormusmoy.constant) {
                        pmut = header.groupe[gr].musmoy;
                        for (int j=0;j<npar;j++) {
                            if (header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].category<2){
                                for (int i=0;i<n;i++) {
                                    phistar[i][nparamcom+k] = pmut*phistar[i][j];
                                }    
                                k++;
                            }
                        }
                    } else {
                        kk=0;while (not ((header.mutparam[kk].groupe == gr)and(header.mutparam[kk].category ==3))) kk++;
                        for (int j=0;j<npar;j++) {
                            if (header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].category<2){
                                for (int i=0;i<n;i++) {
                                    pmut = phistar[i][npar+kk];
                                    phistar[i][nparamcom+k] = pmut*phistar[i][j];
                                }    
                                k++;
                            }
                        }
                    }
                }
            }
        }
        //cout<<"nparcompo = "<<nparcompo<<"   k="<<k<<"\n";
    }
        
/** 
* effectue la sauvegarde des phistars dans le fichier path/ident/phistar.txt
*/
    void savephistar(int n, char* path,char* ident) {
        char *nomphistar ;
        int k;
        nomparam =new string[nparamcom+nparcompo];
        string pp;
        entete="scenario";
        for (int j=0;j<npar;j++) {
            nomparam[j]=string(header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].name);
            entete += centre(header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].name,15);}
        for (int j=npar;j<nparamcom;j++) {
            nomparam[j]=string(header.mutparam[j-npar].name);
            entete += centre(header.mutparam[j-npar].name,15);}
        if (nparcompo>0) {
            k=nparamcom;
            for (int gr=1;gr<header.ngroupes+1;gr++) {
                for (int j=0;j<npar;j++) {
                    if (header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].category<2){
                        pp=header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].name;
                        if (header.groupe[gr].type==0) pp = pp+"(µ+sni)_"+IntToString(gr)+" ";
                        if (header.groupe[gr].type==1) pp = pp+"µseq_"+IntToString(gr)+" ";
                        nomparam[k]=pp;k++;
                        entete += centre(pp,16);
                    }
                }
            }
        }
        nomphistar = new char[strlen(path)+strlen(ident)+20];
        strcpy(nomphistar,path);
        strcat(nomphistar,ident);
        strcat(nomphistar,"_phistar.txt");
        //cout <<nomphistar<<"\n";
        FILE *f1;
        f1=fopen(nomphistar,"w");
        fprintf(f1,"%s\n",entete.c_str());
        for (int i=0;i<n;i++) {
            fprintf(f1,"  %d    ",rt.enrsel[i].numscen);
            for (int j=0;j<nparamcom+nparcompo;j++) fprintf(f1,"  %8.5e  ",phistar[i][j]);
            //if(i<10) for (int j=0;j<nparamcom+nparcompo;j++) printf(" %8.5e",phistar[i][j]);
            fprintf(f1,"\n");
        }
        fclose(f1);
    }

/**
* calcul de la densité par noyau gaussien 
* x : vecteur des abcisses
* y vecteur des 
*/


/**
* lit les paramètres des enregistrements simulés pour l'établissement des distributions a priori'
*/
    void lisimpar(int nsel){
      int bidon,iscen,m,k,kk,qq;
        bool scenOK;
        double pmut;
        if (nsimpar>rt.nrec) nsimpar=rt.nrec;
        simpar = new double*[nsimpar];
        enregC enr;
        enr.stat = new float[rt.nstat];
        enr.param = new float[rt.nparamax];
        int i=-1;
        rt.openfile2();
        while (i<nsimpar-1) {
            bidon=rt.readrecord(&enr);
            scenOK=false;iscen=0;
            while((not scenOK)and(iscen<rt.nscenchoisi)) {
                scenOK=(enr.numscen==rt.scenchoisi[iscen]);
                iscen++;
            }
            if (scenOK) {
              i++;
              simpar[i] = new double[nparamcom+nparcompo];
              m=0;while(enr.numscen!=rt.scenchoisi[m]) m++;
              for (int j=0;j<nparamcom;j++) simpar[i][j] = enr.param[numpar[m][j]];
              if (nparcompo>0) {
                  k=0;
                  for (int gr=1;gr<header.ngroupes+1;gr++) {
                      if (header.groupe[gr].type==0) {
                          if (header.groupe[gr].priormutmoy.constant) {
                              if (header.groupe[gr].priorsnimoy.constant) {
                                  pmut = header.groupe[gr].mutmoy+header.groupe[gr].snimoy;
                                  for (int j=0;j<npar;j++) {
                                      if (header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].category<2){
                                          simpar[i][nparamcom+k] = pmut*enr.param[numpar[m][j]];
                                          k++;
                                      }
                                  }
                              } else {
                                  kk=0;while (not ((header.mutparam[kk].groupe == gr)and(header.mutparam[kk].category ==2))) kk++;
                                  for (int j=0;j<npar;j++) {
                                      if (header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].category<2){
                                          pmut = header.groupe[gr].mutmoy+enr.param[numpar[m][npar+kk]];
                                          simpar[i][nparamcom+k] = pmut*enr.param[numpar[m][j]];
                                          k++;
                                      }
                                  }
                              }
                          } else {
                              if (header.groupe[gr].priorsnimoy.constant) {
                                  kk=0;while (not ((header.mutparam[kk].groupe == gr)and(header.mutparam[kk].category ==0))) kk++;
                                  for (int j=0;j<npar;j++) {
                                      if (header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].category<2){
                                          pmut =enr.param[numpar[0][npar+kk]]+header.groupe[gr].snimoy;
                                          simpar[i][nparamcom+k] = pmut*enr.param[numpar[0][j]];
                                          k++;
                                      }
                                  }
                              } else {
                                  kk=0;while (not ((header.mutparam[kk].groupe == gr)and(header.mutparam[kk].category ==0))) kk++;
                                  qq=0;while (not ((header.mutparam[qq].groupe == gr)and(header.mutparam[qq].category ==2))) qq++;
                                  for (int j=0;j<npar;j++) {
                                      if (header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].category<2){
                                          pmut =enr.param[numpar[m][npar+kk]]+enr.param[numpar[m][npar+qq]];
                                          simpar[i][nparamcom+k] = pmut*enr.param[numpar[m][j]];
                                          k++;
                                      }
                                  }
                              }
                          }
                      } 
                      if (header.groupe[gr].type==1) {    
                          if (header.groupe[gr].priormusmoy.constant) {
                              pmut = header.groupe[gr].musmoy;
                              for (int j=0;j<npar;j++) {
                                  if (header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].category<2){
                                      simpar[i][nparamcom+k] = pmut*enr.param[numpar[m][j]];
                                      k++;
                                  }
                              }
                          } else {
                              kk=0;while (not ((header.mutparam[kk].groupe == gr)and(header.mutparam[kk].category ==3))) kk++;
                              for (int j=0;j<npar;j++) {
                                  if (header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].category<2){
                                      pmut = enr.param[numpar[m][npar+kk]];
                                      simpar[i][nparamcom+k] = pmut*enr.param[numpar[m][j]];
                                      k++;
                                  }
                              }
                          }
                      }
                  }
               }
            }
        }
        rt.closefile();
    }

/**
* calcule la densité à partir de la loi fournie dans le prior
*/
    double* caldensexact(int ncl,double *x,PriorC pr) {
      
        double *dens,xb,som;
        dens = new double[ncl];
        if (pr.loi=="UN") for(int i=0;i<ncl;i++) dens[i]=1.0/(pr.maxi-pr.mini);
        if (pr.loi=="LU") for(int i=0;i<ncl;i++) dens[i]=1.0/(pr.maxi-pr.mini)/x[i];
        if (pr.loi=="NO") for(int i=0;i<ncl;i++) dens[i]=exp(-(x[i]-pr.mean)*(x[i]-pr.mean)/2.0/(pr.sdshape*pr.sdshape))/(pr.sdshape*co);
        if (pr.loi=="LN") for(int i=0;i<ncl;i++) dens[i]=exp(-(log(x[i])/pr.mean)*(log(x[i])/pr.mean)/2.0/(pr.sdshape*pr.sdshape))/(pr.sdshape*co*x[i]);
        if (pr.loi=="GA") for(int i=0;i<ncl;i++) {
            xb=x[i]*pr.sdshape/pr.mean;
            dens[i]=exp((pr.sdshape-1.0)*log(xb)-xb);
        }
        som=0.0;for(int i=0;i<ncl;i++) som +=dens[i];
        for(int i=0;i<ncl;i++) dens[i] /= som;
        return dens;
    }

/**
* calcule la densité à partir d'un échantillon de valeurs'
*/
    double* calculdensite(int ncl,int n, double *x, double **y,int j,bool multithread) { 
        double bw,*dens,sd,*z,denom,som;
        dens = new double[ncl];
        z = new double[n];
        for (int i=0;i<n;i++) z[i]=y[i][j];
        sd =cal_sd(n,z);
        if (sd>0.0) bw=coefbw*exp(-0.2*log((double)n))*sd;
        else bw=1.0;
        //cout<<"sd="<<sd<<"    bw="<<bw<<"\n";
#pragma omp parallel for shared(dens,z,x,bw) private(denom,i) if(multithread)
        for (int j=0;j<ncl;j++) {
            dens[j]=0.0;
            for (int i=0;i<n;i++) dens[j] +=exp(lnormal_dens(z[i],x[j],bw));
            //if(2*j==ncl-1) cout<<" avant denom dens["<<j<<"] = "<< dens[j]<<"\n"; 
            denom=pnorm5((x[ncl-1]-x[j])/bw,0.0,1.0)-pnorm5((x[0]-x[j])/bw,0.0,1.0);
            if (denom>0.0) dens[j] /=denom;
            //if(2*j==ncl-1) cout<<" apres denom dens["<<j<<"] = "<< dens[j]<<"   (denom="<<denom<<")\n"; 
        }
        som=0.0;for (int j=0;j<ncl;j++) {som +=dens[j];}
        if (som>0.0) for (int j=0;j<ncl;j++) dens[j] /=som;
        return dens;
    }

/**
* traitement global du calcul de la densité des paramètres variables
* si le parametre est à valeurs entières avec moins de 30 classes, la densité est remplacée par un histogramme
* sinon la densité est évaluée pour 1000 points du min au max 
*/
    void histodens(int n, bool multithread, char* progressfilename,int* iprog,int* nprog) {
        bool condition;
        FILE *flog;
        pardens = new pardensC[nparamcom+nparcompo];
        for (int j=0;j<nparamcom+nparcompo;j++) {
            pardens[j].ncl=1001;
            condition=false;
            if (j<npar) {  //histparam
                if (header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].category<2) {
                    if (header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].prior.maxi-header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].prior.mini<=30) 
                        pardens[j].ncl=header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].prior.maxi-header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].prior.mini+1;
                }
                pardens[j].xmin=header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].prior.mini;
                pardens[j].xmax=header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].prior.maxi;
                if (header.nconditions>0) {
                    for (int i=0;i<header.nconditions;i++) {
                        condition=((header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].name==header.condition[i].param1)or(header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].name==header.condition[i].param2));
                        if (condition) break;
                    }
                }
            } else if (j<nparamcom){  //mutparam
                pardens[j].xmin=header.mutparam[j-npar].prior.mini;
                pardens[j].xmax=header.mutparam[j-npar].prior.maxi;
            } else {  //parametres composites
                pardens[j].xmin=1E100;pardens[j].xmax=0;
                for (int i=0;i<nsimpar;i++) {
                    if (pardens[j].xmin>simpar[i][j]) pardens[j].xmin=simpar[i][j];
                    if (pardens[j].xmax<simpar[i][j]) pardens[j].xmax=simpar[i][j];
                }
                for (int i=0;i<n;i++) {
                    if (pardens[j].xmin>phistar[i][j]) pardens[j].xmin=phistar[i][j];
                    if (pardens[j].xmax<phistar[i][j]) pardens[j].xmax=phistar[i][j];
                }
            } 
            pardens[j].xdelta = (pardens[j].xmax-pardens[j].xmin)/(double)(pardens[j].ncl-1);
            //cout<<nomparam[j]<<"   xmin="<<pardens[j].xmin<<"   xmax="<<pardens[j].xmax<<"   xdelta="<<pardens[j].xdelta<<"\n";
            pardens[j].x = new double[pardens[j].ncl];
            for (int k=0;k<pardens[j].ncl;k++) pardens[j].x[k]=pardens[j].xmin+k*pardens[j].xdelta;
            if (pardens[j].ncl>31) {
                if ((condition)or(j>=npar)) pardens[j].priord = calculdensite(pardens[j].ncl,nsimpar,pardens[j].x,simpar,j,multithread);
                else pardens[j].priord =caldensexact(pardens[j].ncl,pardens[j].x,header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].prior);
                pardens[j].postd = calculdensite(pardens[j].ncl,n,pardens[j].x,phistar,j,multithread);
            } else {
/*                if ((condition)or(j>=npar)) pardens[j].priord = calculhisto(pardens[j].x,simpar,j,pardens[j].ncl);
                else pardens[j].priord =calhistsexact(header.scenario[rt.scenchoisi[0]-1].histparam[numpar[0][j]].prior,pardens[j].ncl);
                pardens[j].postd = calculhisto(pardens[j].x,phistar,j,pardens[j].ncl);
*/            }
           //cout <<"fin du calcul du parametre "<<j+1<<"  sur "<<nparamcom+nparcompo<<"\n";
        *iprog+=10;flog=fopen(progressfilename,"w");fprintf(flog,"%d %d",*iprog,*nprog);fclose(flog);
        }
     }
 
/**
*calcule les statistiques des paramètres
*/
    void calparstat(int n) {
        double sx,*x;  
        parstat = new parstatC[nparamcom+nparcompo];
        x = new double[n];
        for (int j=0;j<nparamcom+nparcompo;j++) {
            for (int i=0;i<n;i++) x[i] = phistar[i][j];
            sort(&x[0],&x[n]);
            parstat[j].med = x[(int)floor(0.5*n+0.5)-1];
            parstat[j].q025 = x[(int)floor(0.025*n+0.5)-1];
            parstat[j].q050 = x[(int)floor(0.050*n+0.5)-1];
            parstat[j].q250 = x[(int)floor(0.250*n+0.5)-1];
            parstat[j].q750 = x[(int)floor(0.750*n+0.5)-1];
            parstat[j].q950 = x[(int)floor(0.950*n+0.5)-1];
            parstat[j].q975 = x[(int)floor(0.975*n+0.5)-1];
            parstat[j].moy = cal_moy(n,x);
            parstat[j].mod = cal_mode(n,x);
            for (int i=0;i<16-nomparam[j].length();i++) cout<<" ";
            cout<<nomparam[j];
            printf(" %7.2e  %7.2e  %7.2e  %7.2e  %7.2e  %7.2e  %7.2e\n",parstat[j].moy,parstat[j].med,parstat[j].mod,parstat[j].q025,parstat[j].q050,parstat[j].q950,parstat[j].q975);
        }
    }

/**
*sauvegarde les statistiques et les densités des paramètres
*/
    void saveparstat(char *path, char *ident) {
        char *nomfiparstat;
        nomfiparstat = new char[strlen(path)+strlen(ident)+20];
        strcpy(nomfiparstat,path);
        strcat(nomfiparstat,ident);
        strcat(nomfiparstat,"_paramstatdens.txt");
        cout <<nomfiparstat<<"\n";
        FILE *f1;
        f1=fopen(nomfiparstat,"w");
        for (int j=0;j<nparamcom+nparcompo;j++) {
            fprintf(f1,"%s\n",nomparam[j].c_str());
            fprintf(f1,"%8.5e  %8.5e  %8.5e  %8.5e  %8.5e  %8.5e  %8.5e  %8.5e  %8.5e\n",parstat[j].moy,parstat[j].med,parstat[j].mod,parstat[j].q025,parstat[j].q050,parstat[j].q250,parstat[j].q750,parstat[j].q950,parstat[j].q975);
            fprintf(f1,"%d\n",pardens[j].ncl);
            for (int i=0;i<pardens[j].ncl;i++) fprintf(f1,"  %8.5e",pardens[j].x[i]);fprintf(f1,"\n");
            for (int i=0;i<pardens[j].ncl;i++) fprintf(f1,"  %8.5e",pardens[j].priord[i]);fprintf(f1,"\n");
            for (int i=0;i<pardens[j].ncl;i++) fprintf(f1,"  %8.5e",pardens[j].postd[i]);fprintf(f1,"\n");
        }
        fclose(f1);
        strcpy(nomfiparstat,path);
        strcat(nomfiparstat,ident);
        strcat(nomfiparstat,"_psd.txt");
        cout <<nomfiparstat<<"\n";
        f1=fopen(nomfiparstat,"w");
        for (int i=0;i<pardens[0].ncl;i++) {
            for (int j=0;j<nparamcom+nparcompo;j++) fprintf(f1,"%8.5e   %8.5e   %8.5e   ",pardens[j].x[i],pardens[j].priord[i],pardens[j].postd[i]);
            fprintf(f1,"\n");
        }
        fclose(f1);
    }

/** 
* effectue l'estimation ABC des paramètres (directe + régression locale)
*/
    void doestim(char *options,bool multithread) {
        char *datafilename, *progressfilename;
        int rtOK,nstatOK, iprog,nprog;
        int nrec,nsel,ns,ns1,nrecpos;
        string opt,*ss,s,*ss1,s0,s1;
        double  *stat_obs;
        
        FILE *flog;
        
        progressfilename = new char[strlen(path)+strlen(ident)+20];
        strcpy(progressfilename,path);
        strcat(progressfilename,ident);
        strcat(progressfilename,"_progress.txt");
        cout<<"debut doestim  options : "<<options<<"\n";
        opt=char2string(options);
        ss = splitwords(opt,";",&ns);
        for (int i=0;i<ns;i++) { //cout<<ss[i]<<"\n";
            s0=ss[i].substr(0,2);
            s1=ss[i].substr(2);
            if (s0=="s:") {
                ss1 = splitwords(s1,",",&rt.nscenchoisi);
                rt.scenchoisi = new int[rt.nscenchoisi];
                for (int j=0;j<rt.nscenchoisi;j++) rt.scenchoisi[j] = atoi(ss1[j].c_str());
                nrecpos=0;for (int j=0;j<rt.nscenchoisi;j++) nrecpos +=rt.nrecscen[rt.scenchoisi[j]-1];
                cout <<"scenario(s) choisi(s) : ";
                for (int j=0;j<rt.nscenchoisi;j++) {cout<<rt.scenchoisi[j]; if (j<rt.nscenchoisi-1) cout <<",";}cout<<"\n";
            } else {
                if (s0=="n:") {
                    nrec=atoi(s1.c_str());
                    if(nrec>nrecpos) nrec=nrecpos;
                    cout<<"nombre total de jeux de données considérés (pour le(s) scénario(s) choisi(s) )= "<<nrec<<"\n";
                } else {
                    if (s0=="m:") {
                        nsel=atoi(s1.c_str());    
                        cout<<"nombre de jeux de données considérés pour la régression locale = "<<nsel<<"\n";
                    } else {
                        if (s0=="t:") {
                            numtransf=atoi(s1.c_str()); 
                            switch (numtransf) {
                              case 1 : cout <<" pas de transformation des paramètres\n";break;
                              case 2 : cout <<" transformation log des paramètres\n";break;
                              case 3 : cout <<" transformation logit des paramètres\n";break;
                              case 4 : cout <<" transformation log(tg) des paramètres\n";break;
                            }
                        } else {
                            if (s0=="p:") {
                                original=(s1.find("o")!=string::npos);
                                composite=(s1.find("c")!=string::npos);
                                if (original) cout <<"paramètres  originaux  ";
                                if ((s1=="oc")or(s1=="co")) cout <<"et ";
                                if (composite) cout<<"paramètres  composite  ";
                                cout<< "\n";
                            }            
                        }
                    }
                }
            }
        }
        
        nstatOK = rt.cal_varstat();                       cout<<"apres cal_varstat\n";
        stat_obs = header.read_statobs(statobsfilename);  cout<<"apres read_statobs\n";
        nprog=100;iprog=1;
        flog=fopen(progressfilename,"w");fprintf(flog,"%d %d",iprog,nprog);fclose(flog);
        rt.cal_dist(nrec,nsel,stat_obs);                  cout<<"apres cal_dist\n";
        iprog+=8;flog=fopen(progressfilename,"w");fprintf(flog,"%d %d",iprog,nprog);fclose(flog);
        det_numpar();                                     cout<<"apres det_numpar\n";
        nprog=(nparamcom+nparcompo)*10+14;
        recalparam(nsel);                                 cout<<"apres recalparam\n";
        rempli_mat(nsel,stat_obs);                        cout<<"apres rempli_mat\n";
        local_regression(nsel,multithread);               cout<<"apres local_regression\n";
        iprog+=1;flog=fopen(progressfilename,"w");fprintf(flog,"%d %d",iprog,nprog);fclose(flog);
        calphistar(nsel);                                 cout<<"apres calphistar\n";
        savephistar(nsel,path,ident);                     cout<<"apres savephistar\n";
        iprog+=1;flog=fopen(progressfilename,"w");fprintf(flog,"%d %d",iprog,nprog);fclose(flog);
        lisimpar(nsel);                                   cout<<"apres lisimpar\n";
        iprog+=2;flog=fopen(progressfilename,"w");fprintf(flog,"%d %d",iprog,nprog);fclose(flog);
        histodens(nsel,multithread,progressfilename,&iprog,&nprog);                      cout<<"apres histodens\n";
        calparstat(nsel);                                 cout<<"apres calparstat\n";
        saveparstat(path,ident);
        iprog+=1;flog=fopen(progressfilename,"w");fprintf(flog,"%d %d",iprog,nprog);fclose(flog);
    }
