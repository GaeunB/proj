<script>
	let cart = [];
	let products = [
		{id: 1, name: "Apple", image: "https://www.applesfromny.com/wp-content/uploads/2020/05/Jonagold_NYAS-Apples2.png", price: 10, quantity: 1},
		{id: 2, name: "Orange", image: "https://5.imimg.com/data5/VN/YP/MY-33296037/orange-600x600-500x500.jpg", price: 11, quantity: 1},
		{id: 3, name: "Grapes", image: "https://www.aicr.org/wp-content/uploads/2020/01/shutterstock_533487490-640x462.jpg", price: 12, quantity: 1},
	]
	
	const addToCart = (product) => {
		for(let item of cart) {
				if(item.id === product.id) {
					product.quantity += 1
					cart = cart;
					return;
				}
		}
		cart = [...cart, product]
	}
	
	const minusItem = (product) => {
		for(let item of cart) {
				if(item.id === product.id) {
					if(product.quantity > 1 ) {
							product.quantity -= 1
							cart = cart
					} else {
							cart = cart.filter((cartItem) => cartItem != product)
					}
					return;
				}
		}
	}
	
	const plusItem = (product) => {
		for(let item of cart) {
			if(item.id === product.id) {
				item.quantity += 1
				cart = cart;
				return;
			}
		}
	}

	$: total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0)
	
</script>

<div class="m-20 w-full max-w-4xl">
	<h1 class="mb-4 text-2xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl">
		<span class="text-transparent bg-clip-text bg-gradient-to-r to-pink-600 from-pink-400 ">
			장바구니
		</span>
		</h1>
		</div>

<p>There are {cart.length} items in your cart</p>
<div class="product-list">
	{#each products as product}
	<div>
		<div class="image" style="background-image: url({product.image})"></div>
	<h4>{product.name}</h4>
	<p>₹{product.price}</p>
	<button on:click={() => addToCart(product)}>장바구니에 추가하기</button>
	</div>
	{/each}
</div>

<div class="cart-list">
	{#each cart as item }
		{#if item.quantity > 0}
		<div class="cart-item">
			<img width="50" src={item.image} alt={item.name}/>
			<div>{item.quantity}
				<button on:click={() => plusItem(item)}>+</button>
				<button on:click={() => minusItem(item)}>-</button>
			</div>
			<p>₹{item.price * item.quantity}</p>
		</div>
		{/if}
	{/each}
	<div class="total">
		<h4>Total: $ {total}</h4>
	</div>
</div>
<button type="button" class="text-gray-900 bg-gradient-to-r from-red-200 via-red-300 to-yellow-200 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-red-100 dark:focus:ring-red-400 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2"><a href="/pay">구매하기</a></button>




<style>
	.product-list, .cart-item {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
	}
	
	.image {
		height: 150px;
		width: 150px;
		background-size: contain;
		background-position: center;
		background-repeat: no-repeat;
	}
	.total {
		text-align: right;
	}
	
	.cart-list {
		border: 2px solid;
		padding: 10px;
	}
</style>