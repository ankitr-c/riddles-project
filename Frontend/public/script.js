fetch('/get_data')
  .then(res => res.json())
  .then(data => {

    let output = '';

    data.forEach(product => {
      output += `
        <div class="product">
          <img src="${product.img}" width="100">
          <h3>${product.name}</h3>
          <p>${product.desc}</p>
          <b>$${product.price}</b>
        </div>
      `;
    });

    document.getElementById('products').innerHTML = output;

  })
  .catch(err => console.log(err));
