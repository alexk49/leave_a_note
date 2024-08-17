% include('header.tpl', title="New note")
  <body>
    <h1>New note</h1>
    <div id="new-note-container" class="container">
      <form action="/submit" method="POST">
        <div id="note" class="note">
          <div id="top-border" class="top-border"></div>
          <div id="main-note" class="main-note">
            <textarea id="note-text" class="note-text" name="note-text" type="text" maxlength="350"></textarea>
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
