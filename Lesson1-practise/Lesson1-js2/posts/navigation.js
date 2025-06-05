fetch('https://jsonplaceholder.org/posts')
  .then(response => {
    if (!response.ok) {
      throw new Error('Ошибка сети: ' + response.status);
    }
    return response.json(); // Парсим JSON
  })
  .then(data => {
    //console.log(data); // Выводим данные в консоль
    console.log(data.length);
    data.forEach((elem) => {
    var colorArray2 = document.body.getElementsByClassName("news-container");
    const newP = document.createElement('p');
    newP.className = 'title'; 
    newP.textContent  = elem.title;
    const newPContent = document.createElement('p');
    newPContent.className = 'description';
    const newLength = elem.content.slice(0, 250);
    newPContent.textContent  = newLength;
    const newDiv = document.createElement('div');
    newDiv.className = 'container'; 
    const link = document.createElement('a');
    //link.textContent = text;
    //link.href = 'https://dummyimage.com/800x430/FFFFFF/lorem-ipsum.png&text=jsonplaceholder.org';
    const linkReadMore = document.createElement('a');
    linkReadMore.textContent = "ReadMore";
    linkReadMore.href = "C:\\Users\\user\\Desktop\\Lesson1-practise\\Lesson1-js2\\comments\\comments.html";
    const newImg = document.createElement('img');
    newImg.src = 'https://placehold.co/200x200';
    link.appendChild(newImg);
    newDiv.appendChild(link);
    newDiv.appendChild(newP);
    newDiv.appendChild(newPContent);  
    newDiv.appendChild(linkReadMore);
    colorArray2[0].appendChild(newDiv);
    console.log(elem.title)
})
  })
  .catch(error => {
    console.error('Ошибка при запросе:', error);
  });

function createElementsInside() {
  var colorArray2 = document.body.getElementsByClassName("news-container");
  for (var i = 0; i < colorArray2.length; i++) {
    var innerHtml = "";
    for (var j = 0; j < 3; j++) {
      innerHtml += '<div class="element">Element</div>';
    }
    colorArray2[i].innerHTML = innerHtml;
  }
}