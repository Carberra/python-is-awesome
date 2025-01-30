import datetime as dt
from dataclasses import field
from typing import Any

import mesop as me
import pandas as pd
from analytix import Client
from analytix.reports import data

client = Client("secrets.json")


@me.stateclass
class State:
    dimension: str
    filter_key: str
    filter_value: str
    metrics: list[str]
    results_table: dict[str, Any] | None = None
    start_date: dt.date = field(
        default_factory=lambda: dt.date.today() - dt.timedelta(days=28)
    )
    end_date: dt.date = field(default_factory=lambda: dt.date.today())


def on_load(_: me.LoadEvent):
    me.set_theme_mode("dark")


@me.page(path="/reports", on_load=on_load)
def page():
    state = me.state(State)

    with me.box(style=me.Style(min_height="calc(100%)")):
        with me.box(style=me.Style(margin=me.Margin.all(16))):
            me.text("Parameters", type="headline-5")
            parameters_box(state)

            me.text("Result", type="headline-5")
            results_box()


def parameters_box(state):
    with me.box():
        me.select(
            label="Dimension",
            on_selection_change=lambda e: setattr(state, "dimension", e.value),
            options=[
                me.SelectOption(value=dim, label=dim)
                for dim in sorted(data.ALL_DIMENSIONS)
            ],
            appearance="outline",
        )
        me.select(
            label="Filter",
            on_selection_change=lambda e: setattr(state, "filter_key", e.value),
            options=[
                me.SelectOption(value=k, label=k) for k in sorted(data.ALL_FILTERS)
            ],
            appearance="outline",
            style=me.Style(margin=me.Margin(left=16)),
        )
        if state.filter_key:
            me.select(
                label="Filter value",
                on_selection_change=lambda e: setattr(state, "filter_value", e.value),
                options=[
                    me.SelectOption(value=v, label=v)
                    for v in sorted(data.VALID_FILTER_OPTIONS.get(state.filter_key, []))
                ],
                appearance="outline",
                style=me.Style(margin=me.Margin(left=16)),
            )
        me.select(
            label="Metrics",
            on_selection_change=lambda e: setattr(state, "metrics", e.values),
            options=[
                me.SelectOption(value=v, label=v) for v in sorted(data.ALL_METRICS)
            ],
            appearance="outline",
            style=me.Style(margin=me.Margin(left=16)),
            multiple=True,
        )
        me.date_range_picker(
            label="Date range",
            start_date=state.start_date,
            end_date=state.end_date,
            on_change=set_dates,
            appearance="outline",
            style=me.Style(margin=me.Margin(left=16)),
        )
        with me.box():
            me.button(
                label="Fetch report",
                on_click=fetch_report,
                style=me.Style(width="250px", margin=me.Margin(bottom=16)),
                type="flat",
                color="primary",
            )


def results_box():
    with me.box(style=me.Style(width="100%", height="100%")):
        if results_table := me.state(State).results_table:
            me.table(pd.DataFrame.from_dict(results_table))


def set_dates(e: me.DateRangePickerChangeEvent):
    state = me.state(State)
    state.start_date = e.start_date
    state.end_date = e.end_date


def fetch_report(e: me.ClickEvent):
    state = me.state(State)
    state.results_table = (
        client.fetch_report(
            dimensions=[state.dimension] if state.dimension else None,
            filters=(
                {state.filter_key: state.filter_value} if state.filter_key else None
            ),
            metrics=state.metrics or None,
            start_date=state.start_date,
            end_date=state.end_date,
        )
        .to_pandas()
        .to_dict("records")
    )
