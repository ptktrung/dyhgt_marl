"""Shared table helpers. Tables are written as CSV and as Markdown."""
import pathlib
import re
import sys

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
TAB = ROOT / "results" / "tables"
PROC = ROOT / "data" / "processed"
RAW = ROOT / "data" / "raw"
DOCS = ROOT / "docs"


def need(*paths):
    missing = [str(p) for p in paths if not pathlib.Path(p).exists()]
    if missing:
        print("SKIPPED: required input not found:\n  " + "\n  ".join(missing))
        sys.exit(0)


PLUS_MINUS = "±"

# Identifiers that a generic prettifier would get wrong, mostly acronyms,
# proper names and labels that read better with punctuation. Anything absent
# falls through to `prettify`, so a new column or model name still comes out
# readable rather than as raw code.
LABELS = {
    # metrics
    "mae": "MAE", "rmse": "RMSE", "mape": "MAPE", "crps": "CRPS",
    "ece": "ECE", "picp95": "PICP 95", "f1": "F1", "pr_auc": "PR AUC",
    "roc_auc": "ROC AUC", "top1": "Top-1", "top3": "Top-3",
    "root_top1": "Root cause top-1", "root_top3": "Root cause top-3",
    "forecast_mae": "Forecast MAE", "forecast_crps": "Forecast CRPS",
    "forecast_ece": "Forecast ECE", "forecast_picp95": "Forecast PICP 95",
    "reconstruction_mae": "Reconstruction MAE",
    "n_false_alarms": "False alarms", "n_missed": "Missed",
    "n_seeds": "Seeds", "mean_delay_steps": "Mean delay, steps",
    "revenue_recovered_pct": "Revenue recovered, percent",
    "review_workload_pct": "Review workload, percent",
    "missing_rate": "Missing rate",
    # models and baselines
    "dyhgt_marl": "DyHGT-MARL", "mlp": "Multilayer perceptron",
    "hist_gradient_boosting": "Histogram gradient boosting",
    "random_forest_graph_features": "Random forest, graph features",
    "knn_imputer": "k-NN imputer",
    "last_observation_carried_forward": "Last observation carried forward",
    "hour_of_week_climatology": "Hour-of-week climatology",
    "graph_diffusion": "Graph diffusion", "global_mean": "Global mean",
    "rule_based_legacy": "Rule-based legacy",
    "ha": "Climatological mean", "ridge": "Ridge autoregression",
    "gru": "GRU", "dcrnn": "Reduced DCRNN", "stgcn": "Reduced STGCN",
    "transformer": "Temporal Transformer", "dyhgt": "DyHGT-MARL",
    # policies
    "centralized_constrained": "Centralized, constrained",
    "decentralized_constrained": "Decentralized, constrained",
    "centralized_utility_max": "Centralized, utility maximizing",
    "decentralized_utility_max": "Decentralized, utility maximizing",
    "decentralized_constrained_no_abstention":
        "Decentralized, constrained, no abstention",
    "tabular_centralized_constrained": "Tabular, centralized, constrained",
    "tabular_decentralized_constrained": "Tabular, decentralized, constrained",
    "tabular_decentralized_utility_max":
        "Tabular, decentralized, utility maximizing",
    "pg_centralized_constrained": "Policy gradient, centralized, constrained",
    "pg_decentralized_constrained":
        "Policy gradient, decentralized, constrained",
    "pg_decentralized_utility_max":
        "Policy gradient, decentralized, utility maximizing",
    "centralized_decision_policy": "Centralized decision policy",
    # ablation switches
    "full_model": "Full model", "full_policy": "Full policy",
    "static_graph": "Static graph",
    "single_task_fault_only": "Single task, fault head only",
    "no_graph_temporal_only": "No graph, temporal only",
    "no_reliability_conditioning": "No reliability conditioning",
    "no_calibration_term": "No calibration term",
    "no_imputation_head": "No imputation head",
    "no_fairness_constraint": "No fairness constraint",
    "no_abstention_or_escalation": "No abstention or escalation",
    "homogeneous_relations": "Homogeneous relations",
    # scenarios and corpora
    "normal_test": "Normal test", "cascade_active": "Cascade active",
    "topology_change": "Topology change", "topology_closure": "Corridor closure",
    "distribution_shift": "Distribution shift", "gateway_outage": "Gateway outage",
    "hcmc_traffic_data": "HCMC traffic matrix",
    "hcmc_mixed_mobility_data": "HCMC mixed-mobility transactions",
    "integrated_benchmark": "Integrated benchmark",
    # node and relation types
    "sensor_validator": "Sensor validator", "clearing_agent": "Clearing agent",
    "maintenance_agent": "Maintenance agent",
    "r1_travel_connects": "r1, travel connects",
    "r2_senses": "r2, senses",
    "r3_comm_depends": "r3, communication depends",
    "r4_shares_gateway": "r4, shares gateway",
    "r5_provenance": "r5, provenance",
    "r6_operational_authority": "r6, operational authority",
    "r7_functional_similarity": "r7, functional similarity",
    "random_faulty_node": "Random faulty node",
    "highest_centrality_faulty_node": "Highest centrality faulty node",
    # policy measures
    "equal_opportunity_gap": "Equal opportunity gap",
    "demographic_parity_gap": "Demographic parity gap",
    "false_accept_rate": "False accept rate",
    "false_alarm_rate": "False alarm rate",
    "abstention_rate": "Abstention rate",
    "valid_rejection_rate": "Valid rejection rate",
    "decision_error_rate": "Decision error rate",
    "fairness_budget": "Fairness budget",
}


def prettify(s):
    """Turn a code identifier into something a reader can read.

    IEEE Access expects publication-grade labels, and a table that prints
    `pg_centralized_constrained` or `normal_test` exposes the implementation
    rather than the result. Known identifiers come from LABELS and anything
    else falls back to replacing underscores and capitalising the first word,
    so a label added later is still readable without editing this map.
    """
    if not isinstance(s, str):
        return s
    key = s.strip()
    if key in LABELS:
        return LABELS[key]
    if not re.fullmatch(r"[a-z][a-z0-9]*(?:_[a-z0-9]+)*", key):
        return s
    if "_" not in key:
        return s
    words = key.split("_")
    return " ".join([words[0].capitalize()] + words[1:])


def pm(mean, sd, nd=3):
    if sd is None or (isinstance(sd, float) and not np.isfinite(sd)):
        return f"{mean:.{nd}f}"
    return f"{mean:.{nd}f} {PLUS_MINUS} {sd:.{nd}f}"


def agg(df, group, cols, nd=3):
    g = df.groupby(group)[cols].agg(["mean", "std"])
    out = pd.DataFrame(index=g.index)
    for c in cols:
        out[c] = [pm(m, s, nd) for m, s in zip(g[(c, "mean")], g[(c, "std")])]
    return out.reset_index()


def relabel(df):
    """Apply `prettify` to the column headers and to every text cell."""
    out = df.copy()
    out.columns = [prettify(str(c)) for c in out.columns]
    for c in out.columns:
        if out[c].dtype == object:
            out[c] = out[c].map(prettify)
    return out


def emit(df, name, caption, raw=False):
    """Write the table as CSV and as Markdown.

    `raw=True` keeps the identifiers, for the few tables whose first column is
    already prose or mathematics and would be mangled by relabelling.
    """
    TAB.mkdir(parents=True, exist_ok=True)
    if not raw:
        df = relabel(df)
    df.to_csv(TAB / f"{name}.csv", index=False)
    with open(TAB / f"{name}.md", "w", encoding="utf-8") as fh:
        fh.write(f"**{caption}**\n\n")
        fh.write(df.to_markdown(index=False))
        fh.write("\n")
    print(f"wrote results/tables/{name}.csv and .md ({len(df)} rows)")
