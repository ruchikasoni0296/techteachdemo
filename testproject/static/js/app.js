(function () {
    [...document.querySelectorAll(".control")].forEach(button => {
        button.addEventListener("click", function() {
            if(button.dataset.id == "blogs" && !button.classList.contains('active-btn')) {
                document.getElementById("Packages").readOnly = false;
                document.getElementById("Packages").value = "";
            }
            document.querySelector(".active-btn").classList.remove("active-btn");
            this.classList.add("active-btn");
            document.querySelector(".active").classList.remove("active");
            document.getElementById(button.dataset.id).classList.add("active");
        })
    });
    // document.querySelector(".theme-btn").addEventListener("click", () => {
    //     document.body.classList.toggle("light-mode");
    // })
})();


function paymentSuccess(paymentMethod) {
    clearTimeout(this.timeout);
    document.getElementById('paymentSuccessMessage').style.display = 'block';
    document.getElementById('paymentSuccessMessage').innerHTML = 'Successfully paid with ' + paymentMethod + '!';
    this.timeout = setTimeout(function() {
        document.getElementById('paymentSuccessMessage').style.display = 'none';
    }, 5000);
}

function registerForProgram(programName) {
    document.querySelector(".active-btn").classList.remove("active-btn");
    document.querySelector(".active").classList.remove("active");
    document.getElementById("blogs-btn").classList.add("active-btn");
    document.getElementById("blogs").classList.add("active");

    document.getElementById("Packages").readOnly = true;
    document.getElementById("Packages").value = programName;
}