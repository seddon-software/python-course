def create_christmas_card():
     html_content = """
     <!DOCTYPE html>
     <html>
     <head>
          <style>
               body {
                    margin: 0;
                    padding: 20px;
                    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
                    font-family: Arial, sans-serif;
               }
               .card {
                    max-width: 600px;
                    margin: 0 auto;
                    background: linear-gradient(180deg, #87ceeb 0%, #e0f6ff 100%);
                    border-radius: 10px;
                    padding: 40px;
                    text-align: center;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
               }
               .snowflake {
                    color: white;
                    font-size: 2em;
                    margin: 5px;
               }
               h1 {
                    color: #c41e3a;
                    font-size: 2.5em;
                    margin: 20px 0;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
               }
               .message {
                    color: #1a472a;
                    font-size: 1.1em;
                    line-height: 1.6;
                    margin: 30px 0;
               }
               .tree {
                    font-size: 3em;
                    margin: 20px 0;
               }
          </style>
     </head>
     <body>
          <div class="card">
               <div class="snowflake">❄ ❅ ❆ ❄ ❅ ❆</div>
               <h1>Merry Christmas!</h1>
               <div class="tree">🎄</div>
               <p class="message">
                    Wishing you a magical winter season filled with joy, 
                    warmth, and wonderful moments with loved ones.
               </p>
               <div class="snowflake">❄ ❅ ❆ ❄ ❅ ❆</div>
          </div>
     </body>
     </html>
     """
     return html_content

if __name__ == "__main__":
     card = create_christmas_card()
     with open("christmas_card.html", "w") as f:
          f.write(card)
     print("Christmas card created: christmas_card.html")