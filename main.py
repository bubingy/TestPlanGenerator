import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='action')
    generate_parser = subparsers.add_parser('generate')
    summarize_parser = subparsers.add_parser('summarize')

    generate_parser.add_argument(
        '-t',
        '--type',
        dest='project_type',
        choices=['diag-weekly', 'generation-aware']
    )

    summarize_parser.add_argument(
        '-t',
        '--type',
        dest='summarization_type',
        choices=['diag-weekly', 'generation-aware']
    )

    summarize_parser.add_argument(
        '-d',
        '--directory',
        dest='project_root'
    )
    args = parser.parse_args()

    action = args.action

    if action == 'generate':
        import testplan_generator
        project_type = args.project_type
        testplan_generator.generate_test_plan(project_type)

    elif action == 'summarize':
        import testplan_summarization
        summarization_type = args.summarization_type
        project_root = args.project_root
        testplan_summarization.summarize_test_plan(summarization_type, project_root)

    else:
        print(f'unknown action: {action}')
    