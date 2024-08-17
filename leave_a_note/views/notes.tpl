% include('header.tpl', title="Notes")
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
% include("footer.tpl")
