<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Leave a note</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="/static/styles.css" rel="stylesheet" />
  </head>
  <body>
    <h1>Leave a note</h1>
    <p>Leave a note for yourself or the next person!</p>
    <div id="container">
      <form action="/submit" method="POST">
        <div id="note">
          <div id="top-border"></div>
          <div id="main-note">
            <textarea id="note-text" name="note-text" type="text" maxlength="350"></textarea>
          </div>
        </div>
        <div id="note-buttons">
          <input
            type="submit"
            class="note-button"
            id="submit-button"
            value="Submit"
          />
          <input
            type="reset"
            class="note-button"
            id="reset-button"
            value="Reset"
          />
          <div id="counter">0/350</div>
        </div>
      </form>
    </div>
  </body>
  <script src="/static/scripts.js"></script>
</html>
