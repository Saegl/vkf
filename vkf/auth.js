let hash = window.location.hash.substring(1);
console.log(hash);
fetch('/?' + hash, {
    method: "GET",
})
