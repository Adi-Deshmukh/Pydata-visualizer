import os
from jinja2 import Environment, FileSystemLoader


def generate_html_report(profile_dict, output_filename="report.html"):
    # get the path to directory
    script_dir = os.path.dirname(__file__)
    
    # join the current directory path with 'templates' folder name (telling jinja2 where to find report.py)
    template_dir = os.path.join(script_dir, 'templates')
    
    
    env = Environment(loader= FileSystemLoader(template_dir))
    
    template = env.get_template("report.html")
    
    html_content = template.render(overview=profile_dict['overview'],
                                    variables=profile_dict['variables'])
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Report successfully generated: {output_filename}")
