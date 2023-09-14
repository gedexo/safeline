$(document).on('submit', 'form.contact', function(e) {
    e.preventDefault()
    var $this = $(this);
    var data = new FormData(this);
    var action_url = $this.attr('action');
    var reset = $this.hasClass('reset');
    var reload = $this.hasClass('reload');
    var redirect = $this.hasClass('redirect');
    var redirect_url = $this.attr('data-redirect');
    console.log(data)
  
    $.ajax({
        url: action_url,
        type: 'POST',
        data: data,
        cache: false,
        contentType: false,
        processData: false,
        dataType: "json",
  
        success: function(data) {
         
            var status = data.status;
            var title = data.title;
            var message = data.message;
            var pk = data.pk;
  
  
  
            if (status == "true") {
                if (title) {
                    title = title;
                } else {
                    title = "Success";
                }
  
                Swal.fire({
                    title: title,
                    html: message,
                    icon: 'success',
                    confirmButtonText: 'Back to home',
                }).then(function() {
                    if (redirect) {
                        window.location.href = redirect_url;
                    }
                    if (reload) {
                        window.location.reload();
                    }
                    if (reset) {
                        window.location.reset();
                    }
                    window.location.href="/";
                });
                
          
  
            } else {
                if (title) {
                    title = title;
                } else {
                    title = "An Error Occurred";
                }
                Swal.fire({
                    title: title,
                    html: message,
                    icon: "error"
                });
  
            }
        },
        error: function(data) {
            var title = "An error occurred";
            var message = "something went wrong";
            Swal.fire({
                title: title,
                html: message,
                icon: "error"
            });
        }
    });
  });



  $(document).on('submit', 'form.product', function(e) {
    e.preventDefault()
    var $this = $(this);
    var data = new FormData(this);
    var action_url = $this.attr('action');
    var reset = $this.hasClass('reset');
    var reload = $this.hasClass('reload');
    var redirect = $this.hasClass('redirect');
    var redirect_url = $this.attr('data-redirect');
    console.log(data)
  
    $.ajax({
        url: action_url,
        type: 'POST',
        data: data,
        cache: false,
        contentType: false,
        processData: false,
        dataType: "json",
  
        success: function(data) {
         
            var status = data.status;
            var title = data.title;
            var message = data.message;
            var pk = data.pk;
  
  
  
            if (status == "true") {
                if (title) {
                    title = title;
                } else {
                    title = "Success";
                }
  
                Swal.fire({
                    title: title,
                    html: message,
                    icon: 'success',
                    confirmButtonText: 'Back to home',
                }).then(function() {
                    if (redirect) {
                        window.location.href = redirect_url;
                    }
                    if (reload) {
                        window.location.reload();
                    }
                    if (reset) {
                        window.location.reset();
                    }
                    window.location.href="/";
                });
                
          
  
            } else {
                if (title) {
                    title = title;
                } else {
                    title = "An Error Occurred";
                }
                Swal.fire({
                    title: title,
                    html: message,
                    icon: "error"
                });
  
            }
        },
        error: function(data) {
            var title = "An error occurred";
            var message = "something went wrong";
            Swal.fire({
                title: title,
                html: message,
                icon: "error"
            });
        }
    });
  });



  $(document).on('submit', 'form.application', function(e) {
    e.preventDefault()
    var $this = $(this);
    var data = new FormData(this);
    var action_url = $this.attr('action');
    var reset = $this.hasClass('reset');
    var reload = $this.hasClass('reload');
    var redirect = $this.hasClass('redirect');
    var redirect_url = $this.attr('data-redirect');
    console.log(data)
  
    $.ajax({
        url: action_url,
        type: 'POST',
        data: data,
        cache: false,
        contentType: false,
        processData: false,
        dataType: "json",
  
        success: function(data) {
         
            var status = data.status;
            var title = data.title;
            var message = data.message;
            var pk = data.pk;
  
  
  
            if (status == "true") {
                if (title) {
                    title = title;
                } else {
                    title = "Success";
                }
  
                Swal.fire({
                    title: title,
                    html: message,
                    icon: 'success',
                    confirmButtonText: 'Back to home',
                }).then(function() {
                    if (redirect) {
                        window.location.href = redirect_url;
                    }
                    if (reload) {
                        window.location.reload();
                    }
                    if (reset) {
                        window.location.reset();
                    }
                    window.location.href="/";
                });
                
          
  
            } else {
                if (title) {
                    title = title;
                } else {
                    title = "An Error Occurred";
                }
                Swal.fire({
                    title: title,
                    html: message,
                    icon: "error"
                });
  
            }
        },
        error: function(data) {
            var title = "An error occurred";
            var message = "something went wrong";
            Swal.fire({
                title: title,
                html: message,
                icon: "error"
            });
        }
    });
  });