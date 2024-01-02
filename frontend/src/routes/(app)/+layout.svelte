<script lang="ts">
	export let data;
	import { page } from '$app/stores';
	import { Sidebar, SidebarGroup, SidebarItem, SidebarWrapper } from 'flowbite-svelte';
	import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, Button, Input } from 'flowbite-svelte';
  import { Icon } from 'flowbite-svelte-icons';

	let activeUrl: string;
	$: {
		activeUrl = $page.url.pathname;
		console.log(`activeUrl:${activeUrl}`);
	}
	let activeClass = 'flex items-center p-2 text-base font-normal text-primary-900 bg-primary-200 dark:bg-primary-700 rounded-lg dark:text-white hover:bg-primary-100 dark:hover:bg-gray-700';
  let nonActiveClass = 'flex items-center p-2 text-base font-normal text-green-900 rounded-lg dark:text-white hover:bg-green-100 dark:hover:bg-green-700';
</script>


<Navbar let:hidden let:toggle rounded color="teal">
  <NavBrand href="/">
    <img src="logo1.png" class="mr-3 h-6 sm:h-9" alt="프로메테우스 로고" />
    <span class="self-center whitespace-nowrap text-base font-normal dark:text-teal-500">자기소개서요약 프로젝트 팀</span>
  </NavBrand>
  <NavHamburger on:click={toggle} />
  <NavUl {hidden}>
    <NavLi href="/" active={true}>홈</NavLi>
    <NavLi href="#">설정</NavLi>
    </NavUl>
</Navbar>




	<div class="flex-1 justify-center">
		<slot />
	</div>
