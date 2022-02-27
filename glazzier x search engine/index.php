
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="font-awesome-4.7.0\css\font-awesome.min.css">
    <link rel="stylesheet" href="index.css">
    <title>Glazzier</title>

    <style>
            :root {
              --rad: 43rem;
              --dur: 0.3s;
              --color-dark: #2f2f2f;
              --color-light: #fff;
              --color-brand: blue;
              --font-fam: 'Times New Roman', sans-serif;
              --height: 3rem;
              --btn-width: 10rem;
              --bez: cubic-bezier(0, 0, 0.43, 1.49);
            }/*
            body {
              background: var(--color-dark);
              display: flex;
              align-items: center;
              justify-content: center;
              min-height: 100vh;
            }*/
            /*html {
              box-sizing: border-box;
              height: 100%;
            }*/
            *, *::before, *::after {
              box-sizing: inherit;
            }
            form {
              margin-top:20px;
              margin-right: auto;
              margin-left: auto;
              position: relative;
              width: 50rem;
              background: var(--color-brand);
              border-radius: var(--rad);
              box-shadow: 3px 2px 8px #bebebe;
            }
            input, button {
              height: var(--height);
              font-family: var(--font-fam);
              border: 0;
              color: var(--color-dark);
              font-size: 1rem;
            }
            input[type="search"] {
              outline: 0;
              width: 100%;
              background: var(--color-light);
              padding: 0 1.6rem;
              border-radius: var(--rad);
              appearance: none;
              transition: all var(--dur) var(--bez);
              transition-property: width, border-radius;
              z-index: 1;
              position: relative;
            }
            button {
              display: none;
              position: absolute;
              top: 0;
              right: 0;
              width: var(--btn-width);
              font-weight: bold;
              background: var(--color-brand);
              color: white;
              border-radius: 0 var(--rad) var(--rad) 0;
            }
            input:not(:placeholder-shown) {
              border-radius: var(--rad) 0 0 var(--rad);
              width: calc(100% - var(--btn-width));
            }
            input:not(:placeholder-shown) + button {
              display: block;
              padding-left: 10px;
              padding-right: 10px;
            }
            label {
              position: absolute;
              clip: rect(1px, 1px, 1px, 1px);
              padding: 0;
              border: 0;
              height: 1px;
              width: 1px;
              overflow: hidden;
            }
        </style>

</head>
<body>
    <div class="block">
        <div class="top-header">
           <a class="nameHead" href="#" >Glazzier X Search</a> 
           <a class="nameHead" style="font-size: 10pt">This Search Engines Results are from Expanded Queries</a>
            <form role="search" method='GET' action='search_result.php'>
              <label for="search">Search for stuff</label>
              <input id="search" type="search" name='search_query' placeholder="Search the web..." autofocus required />
              <button type="submit" name='btn_search'>Search</button>    
            </form>         
        </div> 
    </div>
</body>
</html>