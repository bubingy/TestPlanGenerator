def summarize_test_plan(summarization_type: str, project_root: str):
    if summarization_type == 'diag-weekly':
        from DiagToolWeekly import summarization
        summarization.summarize_diag_tool_test_plan(project_root)

    if summarization_type == 'generation-aware':
        from GenerationAwareAnalyze import summarization
        summarization.summarize_generation_aware_test_plan(project_root)

    else:
        print(f'unknown summarization type: {summarization_type}')