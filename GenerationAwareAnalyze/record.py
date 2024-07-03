import os
import json

import app
from GenerationAwareAnalyze.generation_aware_test_info import GenerationAwareTestInfo


@app.function_monitor(
    pre_run_msg='write week info to json'
)
def write_week_info_to_json(output_folder: str, week_info: dict) -> None | Exception:
    output_path = os.path.join(output_folder, 'week.json')

    try:
        if os.path.exists(output_path):
            os.remove(output_path)

        with open(output_path, 'w+') as fp:
            json.dump(week_info, fp)
    except Exception as ex:
        return Exception(f'fail to write week info: {ex}')


@app.function_monitor(
    pre_run_msg='write generation aware test info to json'
)
def write_generation_aware_test_info_to_json(output_folder: str,
                                             generation_aware_test_info: GenerationAwareTestInfo) -> None | Exception:
    output_path = os.path.join(output_folder, 'generation_aware.json')

    try:
        if os.path.exists(output_path):
            os.remove(output_path)

        _generation_aware_test_info = {
            'runtime': generation_aware_test_info.runtime_commit_info,
            'blog-samples': generation_aware_test_info.blog_samples_commit_info
        }
        
        with open(output_path, 'w+') as fp:
            json.dump(_generation_aware_test_info, fp)
    except Exception as ex:
        return Exception(f'fail to write generation aware test info: {ex}')