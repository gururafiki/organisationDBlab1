function showCart(cart){
	$('#cart .modal-body').html(cart);
	$('#cart').modal();
}
$('a.level_opener').click(function(){
	if( $(this).hasClass('opened') ) {
		$(this).removeClass('opened');
		// $(this).html('<i class="fa fa-angle-down" aria-hidden="true"></i>');
		$(this).parent().find('>ul').slideUp('fast');
	}
	else {
		$(this).addClass('opened');
		// $(this).html('<i class="fa fa-angle-double-down" aria-hidden="true"></i>');
		$(this).parent().find('>ul').slideDown('fast');
	}
	return false;
});
function getCart(){
	$.ajax({
		url : '/cart/show',
		type: 'GET',
		success: function(res){
			if(!res) alert('Can not find product');
			else showCart(res);
		},
		error:function(){
			alert('Error!');
		}
	});
	return false;
}
$('#cart .modal-body').on('click', '.del-item', function(){
	var id= $(this).data('id');
	$.ajax({
		url : '/cart/del-item',
		data: {id:id},
		type: 'GET',
		success: function(res){
			if(!res) alert('Can not find product');
			else showCart(res);
		},
		error:function(){
			alert('Error!');
		}
	});

});
function clearCart(){
	$.ajax({
		url : '/cart/clear',
		type: 'GET',
		success: function(res){
			if(!res) alert('Can not find product');
			else showCart(res);
		},
		error:function(){
			alert('Error!');
		}
	});
}
$('.add-to-cart').on('click',function(e){
	e.preventDefault();
	var id = $(this).data('id');
	$.ajax({
		url : '/cart/add',
		data: {id:id},
		type: 'GET',
		success: function(res){
			if(!res) alert('Can not find product');
			else showCart(res);
		},
		error:function(){
			alert('Error!');
		}
	});
});



function showProduct(product){
	$('#product-card .modal-body').html(product);
	$('#product-card').modal();
}
$('.add-to-viewed').on('click',function(e){
	e.preventDefault();
	var id = $(this).data('id');
	$.ajax({
		url : '/product/view',
		data: {id:id},
		type: 'GET',
		success: function(res){
			if(!res) alert('Can not find product');
			else showProduct(res);
		},
		error:function(){
			alert('Error!');
		}
	});
});