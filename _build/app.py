# This file generated by Quarto; do not edit by hand.

from __future__ import annotations

from pathlib import Path
from shiny import App, Inputs, Outputs, Session, ui

import pandas as pd
import plotly.graph_objects as go
from shiny import render, reactive, ui
from shinywidgets import output_widget, render_widget
PERCENTILES = {
 0.01: 0,
 0.02: 30156,
 0.03: 50260,
 0.04: 70364,
 0.05: 90971,
 0.06: 100521,
 0.07: 120824,
 0.08: 150000,
 0.09: 160833,
 0.1: 192000,
 0.11: 200000,
 0.12: 201041,
 0.13: 220000,
 0.14: 247590,
 0.15: 252624,
 0.16: 297108,
 0.17: 297108,
 0.18: 301562,
 0.19: 303149,
 0.2: 320000,
 0.21: 326819,
 0.22: 346627,
 0.23: 351822,
 0.24: 361875,
 0.25: 376337,
 0.26: 385000,
 0.27: 396145,
 0.28: 396145,
 0.29: 396145,
 0.3: 400000,
 0.31: 400000,
 0.32: 400000,
 0.33: 402083,
 0.34: 402083,
 0.35: 404199,
 0.36: 415952,
 0.37: 422187,
 0.38: 435255,
 0.39: 445663,
 0.4: 450000,
 0.41: 452343,
 0.42: 454575,
 0.43: 472447,
 0.44: 482499,
 0.45: 495181,
 0.46: 495181,
 0.47: 500000,
 0.48: 500000,
 0.49: 502603,
 0.5: 502604,
 0.51: 505393,
 0.52: 524892,
 0.53: 544698,
 0.54: 550000,
 0.55: 562916,
 0.56: 586036,
 0.57: 594217,
 0.58: 600000,
 0.59: 600000,
 0.6: 603124,
 0.61: 613176,
 0.62: 643734,
 0.63: 653384,
 0.64: 675000,
 0.65: 693253,
 0.66: 700000,
 0.67: 703645,
 0.68: 738827,
 0.69: 753905,
 0.7: 792289,
 0.71: 792289,
 0.72: 800000,
 0.73: 804166,
 0.74: 834322,
 0.75: 854426,
 0.76: 891325,
 0.77: 901671,
 0.78: 940843,
 0.79: 990361,
 0.8: 1000000,
 0.81: 1005207,
 0.82: 1020285,
 0.83: 1090000,
 0.84: 1166040,
 0.85: 1200000,
 0.86: 1256509,
 0.87: 1301743,
 0.88: 1400000,
 0.89: 1485542,
 0.9: 1515745,
 0.91: 1608331,
 0.92: 1782651,
 0.93: 1900000,
 0.94: 2000000,
 0.95: 2104904,
 0.96: 2475904,
 0.97: 2773012,
 0.98: 3030318,
 0.99: 4000000
}

# ========================================================================




def server(input: Inputs, output: Outputs, session: Session) -> None:
    dict(
      icon = "graph-up",
      color = "blue",
      value = "$757.752"
    )

    # ========================================================================

    dict(
      icon = "graph-up",
      color = "warning",
      value = "$502.604"
    )

    # ========================================================================

    ui.input_numeric("sueldo", "Ingrese su sueldo mensual", value=600000)

    # ========================================================================

    @render_widget()
    def nav():
        sueldo = input.sueldo() if input.sueldo() is not None else 0
        DF_CURVA = pd.Series(PERCENTILES)
        aux = DF_CURVA[DF_CURVA<sueldo]
        percentile_sueldo = int(100*DF_CURVA[DF_CURVA>=sueldo].index[0]) if sueldo<=DF_CURVA.iloc[-1] else 99
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=list(DF_CURVA.index), y=list(DF_CURVA.values), hovertemplate='Sueldo mensual: %{y:$,.0f}<extra></extra>'))
        fig.add_trace(go.Scatter(x=list(aux.index), y=list(aux.values), fill='tozeroy', hovertemplate='<extra></extra>'))
        fig.update_layout(
            title = f'{percentile_sueldo} % de las personas ocupadas gana menos que usted.',
            yaxis_title = 'Ingreso mensual',
            xaxis = dict(
                tickmode = 'array',
                tickvals = [.1*i for i in range(11)],
                ticktext = [f'{10*i}%' for i in range(11)]
            ),
            xaxis_tickformat=',.0%',
            yaxis_tickformat=',.0'.replace(',',','),
            yaxis = dict(
                tickmode = 'array',
                tickvals = [500_000*i for i in range(9)],
                ticktext = [f'${500_000*i:,}'.replace(',','.') for i in range(9)]
            ),
            showlegend=False
        )
        fig.update_layout(
            hovermode="x",
            hoverlabel=dict(
                bgcolor="white",
            )
        )
        return fig

    # ========================================================================




_static_assets = ["dashboard_files"]
_static_assets = {"/" + sa: Path(__file__).parent / sa for sa in _static_assets}

app = App(
    Path(__file__).parent / "dashboard.html",
    server,
    static_assets=_static_assets,
)
