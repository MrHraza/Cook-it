window.addEventListener('beforeunload', function(event) { 
    logout();
});

function logout() {
    window.location.href = '/logout';  
}