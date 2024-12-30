def generate_html(entries: list[dict[str, any]]) -> None:
    rows = ''
    for entry in entries:
        row = f"            <!-- {entry['id']} -->"
        if entry['thumbnail_image'] and entry['thumbnail_video']:
            image_source = 'assets/' + entry['id'] + '.jpg'
            video_source = 'assets/' + entry['id'] + '.mp4'
            row += f"""
                <tr onmouseout="{entry['id']}_stop()" onmouseover="{entry['id']}_start()">
                    <td style="padding:20px;width:25%;vertical-align:middle">
                        <div class="one">
                            <div class="two" id='{entry['id']}_video'>
                                <video width=100% height=100% muted autoplay loop>
                                    <source src="{video_source}" type="video/mp4"> Your browser does not support the video tag.
                                </video>
                            </div>
                            <img id='{entry['id']}_image' src='{image_source}' width="160">
                        </div>
                        <script type="text/javascript">
                            function {entry['id']}_start() {{
                                document.getElementById('{entry['id']}_image').style.opacity = "0";
                                document.getElementById('{entry['id']}_video').style.opacity = "1";
                            }}
                
                            function {entry['id']}_stop() {{
                                document.getElementById('{entry['id']}_video').style.opacity = "0";
                                document.getElementById('{entry['id']}_image').style.opacity = "1";
                            }}
                            {entry['id']}_stop()
                        </script>
                    </td>"""
        else:
            image_source = 'assets/' + entry['id'] + '.jpg' if entry['thumbnail_image'] else 'assets/no_img_ph.jpg'
            row += f"""
                <tr>
                    <td style="padding:20px;width:25%;vertical-align:middle">
                        <div class="one">
                            <img src='{image_source}' width="160">
                        </div>
                    </td>"""

        links = []
        if entry['project_page'] is not None:
            links.append(f"<a href='{entry['project_page']}'>project page</a>")
        if entry['paper'] is not None:
            links.append(f"<a href='{entry['paper']}'>paper</a>")
        if entry['code'] is not None:
            links.append(f"<a href='{entry['code']}'>code</a>")
        if entry['video'] is not None:
            links.append(f"<a href='{entry['video']}'>video</a>")
        links = ' / '.join(links)

        row += f"""
                    <td style="padding:20px;width:75%;vertical-align:middle">
                        <span class="papertitle">{entry['title']}</span> &mdash; {entry['year']}
                        <p style="margin:0">{entry['authors']}</p>
                        {links}
                    </td>
                </tr>
    """
        rows += row

    html = f"""
<!DOCTYPE HTML>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>awesome-paper-list</title>
    <link rel="shortcut icon" href="assets/favicon.ico" type="image/x-icon">
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<table style="width:100%;max-width:1000px;border:0px;border-spacing:0px;border-collapse:separate;margin-right:auto;margin-left:auto;"><tbody>
<tr style="padding:0px">
    <td style="padding:0px">
        <table style="width:100%;border:0px;border-spacing:0px;border-collapse:separate;margin-right:auto;margin-left:auto;"><tbody>
        <tr>
            <td style="padding:0px;width:100%;vertical-align:middle">
                <h1>awesome-paper-list</h1>
            </td>
        </tr>
        </tbody></table>
        <table style="width:100%;border:0px;border-spacing:0px;border-collapse:separate;margin-right:auto;margin-left:auto;"><tbody>
        {rows}
        </tbody></table>
        <table style="width:100%;border:0px;border-spacing:0px;border-collapse:separate;margin-right:auto;margin-left:auto;"><tbody>
        <tr>
            <td style="padding:0px">
                <br>
                <p style="text-align:right;font-size:small;">
                    This page was inspired by this <a href="https://github.com/jonbarron/jonbarron_website">template</a> created by <a href="https://jonbarron.info/">Jon Barron</a>.
                </p>
            </td>
        </tr>
        </tbody></table>
    </td>
</tr>
</table>
</body>
</html>
"""
    with open('index.html', 'w') as file:
        file.write(html)
