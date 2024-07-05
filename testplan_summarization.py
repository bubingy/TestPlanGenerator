from DiagToolWeekly import summarization

def summarize_test_plan(summarization_type: str, project_root: str):
    if summarization_type == 'diag-weekly':
        summarization.summarize_diag_tool_test_plan(project_root)

    else:
        print(f'unknown summarization type: {summarization_type}')