var stripe = Stripe('pk_test_51LXnpAF2ppp8RarrrtaYU4b04vi2n9zZW3ZNqJJRVTVLTKnFgbk3TK228tBfHrApdOcxtwiWeDwKlFUm91g6pVe600xJBjyECC')

var elem = document.getElementById('submit');
cliensecret = elem.getAttribute('data-secret')

var elements = stripe.elements();
var style = {
    base: {
        color: "#000",
        lineHeight: '2.4',
        fontSize: '16px'
    }
};
console.log(elements)
var card = elements.create("card", {style: style})
card.mount("#card-element");

card.on('change', function(event) {
    var displayError = document.getElementById('card-errors')
    if (event.error) {
        displayError.textContent = event.error.message;
        $('#card-errors').addClass('alert alert info');
    } else {
        displayError.textContent = '';
        $('#card-errors').removeClass('alert alert info');
    }
})

var form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
    event.preventDefault();

    var custName = document.getElementById("custName").value;
    var custAdd = document.getElementById("custAdd").value;
    var custAdd2 = document.getElementById("custAdd2").value;
    var postCode = document.getElementById("postCode").value;

    console.log(custName)
    console.log(custAdd)
    console.log(custAdd2)
    console.log(postCode)
    
    stripe.confirmCardPayment(cliensecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: custName,
                address: {
                    line1: custAdd,
                    line2: custAdd2
                },
            },
            
        },
    }).then(function(result) {
        if (result.error) {
            console.log('payment error')
            console.log(result.error.message)
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                console.log('payment processed')
                window.location.replace("http://127.0.0.1:8000/payment/orderplaced/")
            }
        }
    })

})