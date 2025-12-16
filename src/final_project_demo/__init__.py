# from .analysis import run_analysis_pipeline, add
# from .cleaning import run_cleaning_pipeling

from final_project_demo.gathering_salaries import (
    add_one,
    calculate_mean,
    create_http_headers,
    parse_salary_table_from_soup,
    scrape_salary_from_url,
    extract_unique_links,
    scrape_with_cloudscraper,
    churn_with_cloudscraper,
)

__all__ = [
    "add_one",
    "calculate_mean",
    "create_http_headers",
    "parse_salary_table_from_soup",
    "scrape_salary_from_url",
    "extract_unique_links",
    "scrape_with_cloudscraper",
    "churn_with_cloudscraper",
]

# your_package/__init__.py

from final_project_demo.analysis import (
    load_and_merge_data,
    filter_players_with_multiple_seasons,
    create_contract_indicators,
    run_mixed_effects_models,
    generate_visualizations,
    run_full_analysis,
)

__all__ = [
    "load_and_merge_data",
    "filter_players_with_multiple_seasons",
    "create_contract_indicators",
    "run_mixed_effects_models",
    "generate_visualizations",
    "run_full_analysis",
]