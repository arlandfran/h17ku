const fs = require("fs");
const path = require("path");
const replace = require("replace-in-file");

const srcRegex = /src=['"](.*?)['"]/g;
const hrefRegex = /href=['"](.*?)['"]/g;
const indexHtmlPath = path.resolve(__dirname, "../dist/index.html");

// take given url and return url_for() wrapped in jinja expression
function sanitize(url) {
  // remove quotes and '/assets/' from url
  const filename = url.replace(/['"]+/g, "").replace("/assets/", "");
  return `{{ url_for('static', filename='${filename}') }}"`;
}

async function replaceAllUrls() {
  let urls = [];
  let flaskUrls = [];
  let indexHtml = fs.readFileSync(indexHtmlPath).toString();

  // find all src / href urls and sanitize them
  for (const match of indexHtml.matchAll(srcRegex)) {
    urls.push(match[0].replace("src=", "").replace(/['"]+/g, ""));
  }

  for (const match of indexHtml.matchAll(hrefRegex)) {
    urls.push(match[0].replace("href=", "").replace(/['"]+/g, ""));
  }

  for (const url in urls) {
    flaskUrls.push(sanitize(urls[url]));
  }

  // replace urls in index.html with sanitized urls
  for (const url in urls) {
    const urlRegex = new RegExp(urls[url]);
    options = {
      files: indexHtmlPath,
      from: urlRegex,
      to: flaskUrls[url],
    };

    try {
      await replace(options);
      console.log("Replaced:", urls[url]);
    } catch (error) {
      console.error("Error occurred:", error);
    }
  }
}

replaceAllUrls();
