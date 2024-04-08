$(document).ready(function() {
    // Ajax for login form submission
    $('#login-form').submit(function(event) {
        event.preventDefault(); // Prevent the default form submission
        var formData = $(this).serialize(); // Serialize form data
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: formData,
            success: function(response) {
                // Redirect to homepage on successful login
                window.location.href = '/'; // Change the URL as needed
            },
            error: function(xhr, status, error) {
                // Display error message if login fails
                $('#login-error').text('Invalid credentials').show();
            }
        });
    });

    // Ajax for sign up form submission
    $('#signup-form').submit(function(event) {
        event.preventDefault(); // Prevent the default form submission
        var formData = $(this).serialize(); // Serialize form data
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: formData,
            success: function(response) {
                // Redirect to homepage on successful sign up
                window.location.href = '/'; // Change the URL as needed
            },
            error: function(xhr, status, error) {
                // Display error message if sign up fails
                $('#signup-error').text('Error occurred. Please try again.').show();
            }
        });
    });

    // Ajax for review form submission
    $('#review-form').submit(function(event) {
        event.preventDefault(); // Prevent the default form submission
        var formData = $(this).serialize(); // Serialize form data
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: formData,
            success: function(response) {
                // Show success message and clear form
                $('#review-success').text('Review submitted successfully').show();
                $('#review-form')[0].reset();
            },
            error: function(xhr, status, error) {
                // Display error message if review submission fails
                $('#review-error').text('Error occurred. Please try again.').show();
            }
        });
    });
    
    // Ajax for teacher deletion
    $('.delete-teacher').click(function(event) {
        event.preventDefault(); // Prevent the default link behavior
        var deleteUrl = $(this).attr('href'); // Get the delete URL
        var listItem = $(this).closest('li'); // Get the parent list item
        $.ajax({
            type: 'POST',
            url: deleteUrl,
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}' // Include CSRF token
            },
            success: function(response) {
                // Remove the list item on successful deletion
                listItem.remove();
            },
            error: function(xhr, status, error) {
                // Display error message if deletion fails
                alert('Error occurred while deleting teacher.');
            }
        });
    });

    // Ajax for student deletion
    $('.delete-student').click(function(event) {
        event.preventDefault(); // Prevent the default link behavior
        var deleteUrl = $(this).attr('href'); // Get the delete URL
        var listItem = $(this).closest('li'); // Get the parent list item
        $.ajax({
            type: 'POST',
            url: deleteUrl,
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}' // Include CSRF token
            },
            success: function(response) {
                // Remove the list item on successful deletion
                listItem.remove();
            },
            error: function(xhr, status, error) {
                // Display error message if deletion fails
                alert('Error occurred while deleting student.');
            }
        });
    });
});
