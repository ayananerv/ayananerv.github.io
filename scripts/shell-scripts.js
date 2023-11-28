// script.js

var markdownURL = '../markdown/shell-scripts.md';

// 获取Markdown文件内容
fetch(markdownURL)
  .then(response => response.text())
  .then(markdownContent => {
    // 将Markdown转换为HTML
    var htmlContent = marked.parse(markdownContent);

    // 将HTML内容插入到指定的元素中
    document.getElementById('markdown-content').innerHTML = htmlContent;
  })
  .catch(error => {
    console.error('Error fetching Markdown file:', error);
  });