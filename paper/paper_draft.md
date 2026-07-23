---
tags: [#paper/draft, #latex/source]
alias: "Paper Draft (LaTeX Source View)"
---

# 📄 A Theory of Computational Coupling Between Intelligent Systems — LaTeX Source

> [!info] **Main LaTeX Source File:** [[paper/main.tex|paper/main.tex]]
> **Compiled Output PDF:** [[paper/output/paper.pdf|paper/output/paper.pdf]]
> **References Database:** [[paper/references.bib|paper/references.bib]]

```latex
\documentclass[11pt]{article}

\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{titlesec}
\usepackage{booktabs}
\usepackage{array}

\hypersetup{
    colorlinks=true,
    linkcolor=blue!50!black,
    citecolor=blue!50!black,
    urlcolor=blue!50!black
}

\newtheorem{prediction}{Prediction}
\newtheorem{definitionbox}{Definition}

\title{\Large \textbf{A Theory of Computational Coupling Between Intelligent Systems}\\[4pt]
\large Toward a General Foundation for Brain-to-Brain Communication}

\author{\textbf{Ashok Pasala} \\[2pt] \small VIT-AP University \\[2pt] \small \texttt{Independent Research --- Working Draft v0.2.0}}

\date{July 23, 2026}

\begin{document}

\maketitle

\begin{abstract}
\noindent
Efforts toward brain-to-brain communication (BBI) and related brain-computer interface (BCI) paradigms have largely proceeded by designing communication \emph{protocols} --- fixed encodings, tokenizations, or aligned representational spaces --- without first establishing what quantity such a protocol should maximize, or how to measure whether it has succeeded. We introduce a general theory of \textbf{computational coupling} between intelligent systems --- biological or artificial --- that defines a substrate-independent, directed, information-theoretic quantity (\textbf{coupling capacity}) governing how predictively entangled two systems' internal state trajectories can become, given a bandwidth- and structure-constrained interface between them. We derive three falsifiable predictions from this theory, propose estimators suitable for both simulated multi-agent systems and biological recordings, and outline how brain-to-brain communication, communication protocols, and language itself are best understood as special-case applications of this more general quantity, rather than as the object of study in themselves.
\end{abstract}

\section{Introduction}
Prior to 1948, telecommunications engineering possessed extensive practical technique but no rigorous mathematical definition of \emph{information} or of a channel's fundamental capacity. Claude Shannon's landmark contribution was not a specific telegraph device or radio modem, but a \emph{measurement theory} that specified the theoretical upper bound of error-free transmission over any noisy medium.

We argue that current efforts in Brain-to-Brain Communication (BBI) and Brain-Computer Interfaces (BCIs) occupy an analogous position today. Substantial engineering ingenuity is devoted to designing tokenization schemes, neural decoders, and aligned embedding spaces, yet the field lacks a governing quantity that specifies:
\begin{enumerate}
    \item What fundamental quantity is being optimized across a brain-to-brain link?
    \item What are the theoretical upper bounds on information exchange between two dynamic, non-stationary neural manifolds?
\end{enumerate}

\section{Formal Framework}
We define the directed coupling from system $i$ to system $j$ as the Transfer Entropy (directed information):
\begin{equation}
\mathrm{TE}_{i \to j}(\Delta; g) \;=\; I\big(x_i(t)\, ;\, x_j(t+\Delta) \,\big|\, x_j(\le t)\big)
\end{equation}

\begin{definitionbox}[Coupling Capacity]
The \textbf{coupling capacity} from system $i$ to system $j$ is the supremum of directed coupling over admissible interfaces:
\begin{equation}
C(i \to j) \;=\; \sup_{g \,\in\, \mathcal{G}} \; \mathrm{TE}_{i \to j}(\Delta; g)
\end{equation}
\end{definitionbox}

\section{Falsifiable Predictions}
\begin{prediction}[Capacity--Bandwidth Law]
$C(i \to j; B)$ is monotonically increasing and concave in $B$, saturating at $\min\big(\dim_{\mathrm{eff}}(\mathcal{M}_i),\, \dim_{\mathrm{eff}}(\mathcal{M}_j)\big)$.
\end{prediction}

\begin{prediction}[Self-Predictive Accuracy Governs Capacity Efficiency]
$C(i \to j)/B$ is monotonically increasing in $R_i$ and $R_j$ jointly.
\end{prediction}

\begin{prediction}[Asymmetry Tracks Role]
The asymmetry index $A = \frac{C(i \to j) - C(j \to i)}{C(i \to j) + C(j \to i)}$ correlates with externally defined task roles.
\end{prediction}

\end{document}
```
