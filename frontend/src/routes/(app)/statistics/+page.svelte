<script>
  let cartItems = [
    { id: 1, name: '여름용 청바지', price: 10, quantity: 2 },
    { id: 2, name: '하늘하늘 블라우스', price: 20, quantity: 1 },
    { id: 3, name: '캡모자', price: 15, quantity: 3 }
  ];

  function removeItem(id) {
    cartItems = cartItems.filter(item => item.id !== id);
  }
</script>


<div class="m-20 w-full max-w-2xl">
	<h1 class="mb-4 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl">
		<span class="text-transparent bg-clip-text bg-gradient-to-r to-pink-600 from-pink-400 ">
			장바구니
		</span>
		</h1>
		</div>

<section class="mb-20">
{#each cartItems as item (item.id)}
  <div class="cart-item mb-20">
    <div class="item-details">
      <p>{item.name}</p>
      <p>가격: ${item.price}</p>
      <p>수량: {item.quantity}</p>
    </div>
    <button on:click={() => removeItem(item.id)}>삭제</button>
  </div>
{/each}
<div class="flex justify-center items-center">
<button type="button" class="w-full text-gray-900 bg-pink-400 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-red-100 dark:focus:ring-red-400 font-medium rounded-lg text-sm px-5 py-5 text-center mr-2 mb-2">총 금액: ${cartItems.reduce((total, item) => total + item.price * item.quantity, 0)} 구매하기</button>
</div>
</section>

<style>
  .cart-item {
    display: flex;
    align-items: center;
    border: 1px solid #ccc;
    padding: 10px;
    margin: 20px;
  }
  .item-details {
    flex: 1;
    margin-right: 10px;
  }
  button {
    background-color: #F17EB8;
    color: white;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
    height: 50px;
    margin: 0 20px;

  }
</style>
