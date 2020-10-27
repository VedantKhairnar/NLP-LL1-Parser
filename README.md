# NLP-LL1-Parser


![Stars](https://img.shields.io/github/stars/VedantKhairnar/NLP-LL1-Parser.svg?style=social)
![Forks](https://img.shields.io/github/forks/VedantKhairnar/NLP-LL1-Parser.svg?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/VedantKhairnar/NLP-LL1-Parser.svg)
![Language](https://img.shields.io/github/languages/top/VedantKhairnar/NLP-LL1-Parser.svg)
[![Say Thanks!](https://img.shields.io/badge/Say-Thanks!-yellow.svg)](https://vedantkhairnar.ml)
[![HitCount](http://hits.dwyl.io/VedantKhairnar/NLP-LL1-Parser.svg)](http://hits.dwyl.io/VedantKhairnar/Face-Recognition-based-Attendance-System)
![Issues](https://img.shields.io/github/issues/VedantKhairnar/NLP-LL1-Parser)
![PRsWelcome](https://img.shields.io/badge/PRs-welcome-informational)

``
Relating Natural language processing (NLP) and Compiler
``


Validating natural language sentenes: Consider a natural language grammar and construct the LL(1) table and check if the user entered statement is correct gramatically.


## Steps to check:
- Change the expression in ll_parsetools.py
- Run ll.parsetools.py

## Automata
```
S : NP_Sg VP_Sg | NP_Pl VP_Pl
NP : NP_Pl | NP_Sg
NP_Sg : N_Sg | Det_Sg N_Sg | Det_Both N_Sg | Adj N_Sg | Det_Sg Adj N_Sg | Det_Both Adj N_Sg| PropN_Sg
NP_Pl : N_Pl | Det_Pl N_Pl | Det_Both N_Pl | Adj N_Pl | Det_Pl Adj N_Pl | Det_Both Adj N_Pl| PropN_Pl
VP_Sg : IV_Pres_Sg | IV_Past | TV_Pres_Sg | TV_Past | TV_Pres_Sg NP | TV_Past NP | Adv IV_Pres_Sg | Adv IV_Past | Adv TV_Pres_Sg NP | Adv TV_Past NP
VP_Pl : IV_Pres_Pl | IV_Past | TV_Pres_Pl | TV_Past | TV_Pres_Pl NP | TV_Past NP | Adv IV_Pres_Pl | Adv IV_Past | Adv TV_Pres_Pl NP | Adv TV_Past NP
N_Pl : girls | boys | children | cars | apples | dogs
Adj : good | bad | beautiful | innocent
Adv : happily | sadly | nicely
N_Sg : dog | girl | car | child | apple | elephant
PropN_Sg : rashmi | piyumika
PropN_Pl : they | i
Det_Sg : this | every | a | an
Det_Pl : these | all
Det_Both : some | the | several
IV_Pres_Sg : dissappeares | walks
TV_Pres_Sg : sees | likes |eat
IV_Pres_Pl : dissappear | walk
TV_Pres_Pl : see | like
IV_Past : dissappeared | walked
TV_Past : saw | liked | ate | shot
```

### Team Members:

1. [Vedant Khairnar](https://vedantkhairnar.ml/)
2. [Ananya Singh](#)
3. [Shrijeet Shivdekar](#)
4. [Kheevar Chaudhary](#)
