<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Leave a note - notes</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="/static/styles.css" rel="stylesheet" />
  </head>
  <body>
    <h1>Notes</h1>
    <div id="notes-container" class="container">
    %for note in notes:
        <div id="note-{{note[0]}}" class="note">
          <div id="top-border-{{note[0]}}" class="top-border">{{note[1]}}</div>
          <div id="main-note-{{note[0]}}" class="main-note">
            <div id="note-text-{{note[0]}}" class="note-text">{{note[2]}}</div>
          </div>
        </div>
    %end
    </div>
  </body>
  <script src="/static/scripts.js"></script>
</html>
