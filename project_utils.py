
from IPython.display import display, HTML, Math

def display_as_html(text):
    """ Cette fonction affiche du texte comme du html """
    display(HTML(text))

def compute_as_html_table(dico: dict):

    render = "<table style='font-size: 1.2em; font-wight: Arial; width: 500px;'>"
    render += """
    <thead>
        <tr>
            <th style='text-align: left !important;'>Interval</th>
            <th style='text-align: left !important;'>Number of solutions</th>
        </tr>
    </thead><tboby>"""

    for key, value in dico.items():
        render += f"""
        <tr>
            <td style='text-align: left; padding: 10px;'>{key}</td>
            <td style='text-align: left; padding: 10px;'>{value}</td>
        </tr>"""
    render += "</tboby></table>"
    return render