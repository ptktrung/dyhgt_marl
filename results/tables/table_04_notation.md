**Table IV. Notation used throughout the paper.**

| Symbol                                                             | Meaning                                                                           |
|:-------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| $G_t = (V_t, E_t, R, X_t, A_t)$                                    | dynamic heterogeneous graph at step $t$                                           |
| $V_t$                                                              | node set at step $t$, five node types                                             |
| $E_t$                                                              | edge set at step $t$, typed by relation                                           |
| $R$                                                                | relation types, seven in the schema and four used for message passing             |
| $X_t$                                                              | node feature matrix at step $t$                                                   |
| $A_t$                                                              | stack of relation adjacency matrices active at step $t$                           |
| $\tilde{A}_{ij}$                                                   | normalized adjacency weight between nodes $i$ and $j$                             |
| $N$                                                                | number of transit nodes, 28                                                       |
| $T$                                                                | number of time steps, 2880 at 15 minute resolution                                |
| $r$                                                                | relation index                                                                    |
| $p_0$, $\tau$                                                      | cascade base probability and temporal decay constant                              |
| $W_Q^r, W_K^r, W_V^r$                                              | relation specific query, key and value projections                                |
| $\alpha_{ij}^{(r,t)}$                                              | attention weight from node $j$ to node $i$ under relation $r$ at step $t$         |
| $b_{ij}^{(r,t)}$                                                   | learned edge bias for the edge active in the snapshot at step $t$                 |
| $q_i$                                                              | reliability score of node $i$, in the unit interval                               |
| $\psi(q_i, q_j)$                                                   | reliability conditioning term of the attention logit                              |
| $w_1^r, w_2^r, w_3^r$                                              | coefficients of the reliability conditioning term                                 |
| $d$                                                                | hidden dimension of the encoder                                                   |
| $\phi_k$                                                           | $k$-th eigenvector of the normalized graph Laplacian                              |
| $\mathrm{PE}(v_i)$                                                 | spectral positional encoding of node $i$                                          |
| $y_{i,t}$                                                          | true travel time at node $i$ and step $t$, minutes                                |
| $\hat{y}_{i,t}$                                                    | reconstructed travel time at node $i$ and step $t$                                |
| $m_{i,t}$                                                          | missingness indicator, one if the observation is absent                           |
| $f_{i,t}$                                                          | fault label at node $i$ and step $t$                                              |
| $z_{i,t}$                                                          | fault logit emitted for node $i$ at step $t$                                      |
| $\sigma(\cdot)$                                                    | logistic function                                                                 |
| $s_{m,j}$                                                          | root cause score for node $j$ in record $m$                                       |
| $c_m$                                                              | labelled root node of record $m$                                                  |
| $\pi_{i,k}, \mu_{i,k}, \sigma_{i,k}$                               | mixture weight, mean and scale of component $k$                                   |
| $K$                                                                | number of mixture components, three                                               |
| $h(u)$                                                             | Huber loss, quadratic below unit deviation and linear beyond it                   |
| $\mathcal{B}$                                                      | node-steps in the training batch                                                  |
| $\mathcal{B}'$                                                     | node-steps in the batch that have a successor in the window                       |
| $\mathcal{E}$                                                      | training records carrying a labelled cascade root                                 |
| $\mathcal{M}$                                                      | node-steps whose input value was deliberately masked                              |
| $L_{total}$                                                        | multi-task objective                                                              |
| $\lambda_f, \lambda_r, \lambda_m, \lambda_y, \lambda_c, \lambda_s$ | weights of the fault, root cause, mask, forecast, calibration and stability terms |
| $a \in \mathcal{A}$                                                | action from accept, reject, impute, corroborate, defer, isolate, escalate         |
| $a_i$                                                              | acceptance indicator for record $i$                                               |
| $v_i$                                                              | validity indicator, one if record $i$ is genuinely valid                          |
| $U_t$                                                              | realized financial outcome of decision $t$, in currency units                     |
| $R'_t$                                                             | shaped reward the agent receives at decision $t$                                  |
| $\kappa$                                                           | scale applied to the financial outcome in the shaped reward                       |
| $\gamma$                                                           | discount factor of the decision process                                           |
| $\ell(a)$                                                          | nominal latency of action $a$, milliseconds, a simulator assumption               |
| $B$                                                                | number of decisions in an episode                                                 |
| $\mathrm{TPR}_g$                                                   | share of genuinely valid records accepted in group $g$                            |
| $C_{fair}, C_{latency}, C_{risk}$                                  | realized fairness, latency and risk costs                                         |
| $\epsilon_f, \epsilon_l, \epsilon_r$                               | budgets for the three constraints                                                 |
| $\lambda_f^{dual}, \lambda_l^{dual}, \lambda_r^{dual}$             | dual variables of the constrained problem                                         |
| $\eta_f, \eta_l$                                                   | dual ascent step sizes, 0.6 and 0.1                                               |
| $w_p, w_c$                                                         | weights of the two per-decision fairness surrogate events, 0.5 and 0.05           |
