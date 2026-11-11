"""Table IV: notation. Curated list, written by script for consistency.

The symbol column is LaTeX, so the document build turns each entry into Office
Math Markup and the table reads as mathematics rather than as the ASCII
transliteration it used to carry. `raw=True` keeps the label prettifier away
from the column, which would otherwise try to read the markup as an identifier.
"""
from _common import emit
import pandas as pd

NOTATION = [
    # graph
    (r"$G_t = (V_t, E_t, R, X_t, A_t)$", "dynamic heterogeneous graph at step $t$"),
    (r"$V_t$", "node set at step $t$, five node types"),
    (r"$E_t$", "edge set at step $t$, typed by relation"),
    (r"$R$", "relation types, seven in the schema and four used for message passing"),
    (r"$X_t$", "node feature matrix at step $t$"),
    (r"$A_t$", "stack of relation adjacency matrices active at step $t$"),
    (r"$\tilde{A}_{ij}$", "normalized adjacency weight between nodes $i$ and $j$"),
    (r"$N$", "number of transit nodes, 28"),
    (r"$T$", "number of time steps, 2880 at 15 minute resolution"),
    (r"$r$", "relation index"),
    (r"$p_0$, $\tau$", "cascade base probability and temporal decay constant"),
    # encoder
    (r"$W_Q^r, W_K^r, W_V^r$", "relation specific query, key and value projections"),
    (r"$\alpha_{ij}^{(r,t)}$",
     "attention weight from node $j$ to node $i$ under relation $r$ at step $t$"),
    (r"$b_{ij}^{(r,t)}$", "learned edge bias for the edge active in the snapshot at step $t$"),
    (r"$q_i$", "reliability score of node $i$, in the unit interval"),
    (r"$\psi(q_i, q_j)$", "reliability conditioning term of the attention logit"),
    (r"$w_1^r, w_2^r, w_3^r$", "coefficients of the reliability conditioning term"),
    (r"$d$", "hidden dimension of the encoder"),
    (r"$\phi_k$", "$k$-th eigenvector of the normalized graph Laplacian"),
    (r"$\mathrm{PE}(v_i)$", "spectral positional encoding of node $i$"),
    # heads and targets
    (r"$y_{i,t}$", "true travel time at node $i$ and step $t$, minutes"),
    (r"$\hat{y}_{i,t}$", "reconstructed travel time at node $i$ and step $t$"),
    (r"$m_{i,t}$", "missingness indicator, one if the observation is absent"),
    (r"$f_{i,t}$", "fault label at node $i$ and step $t$"),
    (r"$z_{i,t}$", "fault logit emitted for node $i$ at step $t$"),
    (r"$\sigma(\cdot)$", "logistic function"),
    (r"$s_{m,j}$", "root cause score for node $j$ in record $m$"),
    (r"$c_m$", "labelled root node of record $m$"),
    (r"$\pi_{i,k}, \mu_{i,k}, \sigma_{i,k}$", "mixture weight, mean and scale of component $k$"),
    (r"$K$", "number of mixture components, three"),
    (r"$h(u)$", "Huber loss, quadratic below unit deviation and linear beyond it"),
    # index sets
    (r"$\mathcal{B}$", "node-steps in the training batch"),
    (r"$\mathcal{B}'$", "node-steps in the batch that have a successor in the window"),
    (r"$\mathcal{E}$", "training records carrying a labelled cascade root"),
    (r"$\mathcal{M}$", "node-steps whose input value was deliberately masked"),
    # objective
    (r"$L_{total}$", "multi-task objective"),
    (r"$\lambda_f, \lambda_r, \lambda_m, \lambda_y, \lambda_c, \lambda_s$",
     "weights of the fault, root cause, mask, forecast, calibration and stability terms"),
    # decision layer
    (r"$a \in \mathcal{A}$",
     "action from accept, reject, impute, corroborate, defer, isolate, escalate"),
    (r"$a_i$", "acceptance indicator for record $i$"),
    (r"$v_i$", "validity indicator, one if record $i$ is genuinely valid"),
    (r"$U_t$", "realized financial outcome of decision $t$, in currency units"),
    (r"$R'_t$", "shaped reward the agent receives at decision $t$"),
    (r"$\kappa$", "scale applied to the financial outcome in the shaped reward"),
    (r"$\gamma$", "discount factor of the decision process"),
    (r"$\ell(a)$", "nominal latency of action $a$, milliseconds, a simulator assumption"),
    (r"$B$", "number of decisions in an episode"),
    (r"$\mathrm{TPR}_g$", "share of genuinely valid records accepted in group $g$"),
    (r"$C_{fair}, C_{latency}, C_{risk}$", "realized fairness, latency and risk costs"),
    (r"$\epsilon_f, \epsilon_l, \epsilon_r$", "budgets for the three constraints"),
    (r"$\lambda_f^{dual}, \lambda_l^{dual}, \lambda_r^{dual}$",
     "dual variables of the constrained problem"),
    (r"$\eta_f, \eta_l$", "dual ascent step sizes, 0.6 and 0.1"),
    (r"$w_p, w_c$", "weights of the two per-decision fairness surrogate events, 0.5 and 0.05"),
]


def main():
    emit(pd.DataFrame(NOTATION, columns=["Symbol", "Meaning"]),
         "table_04_notation", "Table IV. Notation used throughout the paper.",
         raw=True)


if __name__ == "__main__":
    main()
