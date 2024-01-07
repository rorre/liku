# Tailwind CSS

Tailwind CSS is a utility-first CSS framework for rapidly building modern websites without ever leaving your HTML.

## Setting Up

Setting up Tailwind CSS for your project inherently depends on your web framework, notably _where_ your CSS static
files will be. However, I will provide an example set up guide for you to have a base on.
**Ensure you have Node.js installed or the [standalone CLI](https://tailwindcss.com/blog/standalone-cli) installed in your PATH**.

!!! note

    This guide assumes:

    - Your Python source code is in a folder called `app`
    - Your input CSS file at `app/css/base.css`
    - Your static directory is at `app/static`
    - The output file will be at `app/static/style.css`

1. Install Tailwind CSS
   ```sh
   npm install -D tailwindcss  # Skip if you already use the CLI
   npx tailwindcss init  # Use just tailwindcss if you use CLI
   ```
2. Inside `tailwind.config.js`, add your Python source code directory to `content`
   ```js
   /** @type {import('tailwindcss').Config} */
   module.exports = {
     content: ["./app/**/*.{py,html,js}"],
     theme: {
       extend: {},
     },
     plugins: [],
   };
   ```
3. Add Tailwind CSS directives to your input CSS file
   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```
4. Start Tailwind CLI build
   ```sh
   # Use just tailwindcss if you use CLI
   npx tailwindcss -i ./app/css/base.css -o ./app/static/style.css --watch
   ```
5. If you are using Visual Studio Code, follow next steps to get Intellisense working

## Code Configuration

Because Liku is not using HTML syntax, Tailwind CSS Intellisense does not work as expected.
To fix this, add the following custom regex rule for Tailwind CSS plugin in your Code config:

```json title="settings.json"
{
  "tailwindCSS.experimental.classRegex": [
    "[\"']class_[\"'] *: *[\"']([^\"']*)",
  ]
}
```

<figure>
    <img src="https://d.rorre.me/a3IwVJgI/Code_cjqkUkkdpi.gif">
</figure>
