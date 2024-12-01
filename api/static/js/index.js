function visitAPI(linkval) {
    if (linkval === 'link1') {
        const i1 = document.getElementById("i1");
    
        // Regular expression to check for "AT" followed by 3 digits
        const regex = /^AT\d{3}$/;
    
        // Validate the input value using the regex
        if (regex.test(i1.value)) {
            window.open(`/api/activities/activity-type/${i1.value}`, "_blank");
        } else {
            alert("Please enter a valid value in the format 'AT' followed by 3 digits (e.g., AT001).");
        }
    }
    else if (linkval === 'link2') {
        const i2 = document.getElementById("i2");
        // Check if i2 is a positive number greater than 0
        if (i2.value > 0) {
            window.open(`/api/activities/limit/${i2.value}`, "_blank");
        } else {
            alert("Please enter a number greater than 0.");
        }
    }
    else if (linkval === 'link3') {
        const i3a = document.getElementById("i3a");
        const i3b = document.getElementById("i3b");
    
        // Function to validate the YYYY-MM-DD format and check if the date is valid
        function isValidDate(dateStr) {
            const regex = /^\d{4}-\d{2}-\d{2}$/; // Regex for YYYY-MM-DD
            if (!regex.test(dateStr)) return false;
    
            // Check if the string can be converted to a valid date
            const date = new Date(dateStr);
            return !isNaN(date.getTime()) && dateStr === date.toISOString().split('T')[0];
        }
    
        // Validate both dates
        if (isValidDate(i3a.value) && isValidDate(i3b.value)) {
            window.open(`/api/activities/date/${i3a.value}/${i3b.value}`, "_blank");
        } else {
            alert("Please enter valid dates in YYYY-MM-DD format.");
        }
    }
    else if (linkval === 'link4') {
        const i4 = document.getElementById("i4");
    
        // Regular expression to check for "AT" followed by 3 digits
        const regex = /^AT\d{3}$/;
    
        // Validate the input value using the regex
        if (regex.test(i4.value)) {
            window.open(`/api/activities/activity-type/${i4.value}`, "_blank");
        } else {
            alert("Please enter a valid value in the format 'AT' followed by 3 digits (e.g., AT001).");
        }
    }
    else if (linkval === 'link5') {
        const i5 = document.getElementById("i5");
        // Check if i5 is a positive number greater than 0
        if (i5.value > 0) {
            window.open(`/api/performance-metrics/limit/${i5.value}`, "_blank");
        } else {
            alert("Please enter a number greater than 0.");
        }
    }
    else if (linkval === 'link6') {
        const i6 = document.getElementById("i6");
        // Check if i6 is a positive number greater than 0
        if (i6.value > 0) {
            window.open(`/api/lap-metrics/limit/${i6.value}`, "_blank");
        } else {
            alert("Please enter a number greater than 0.");
        }
    }
    else if (linkval === 'link7') {
        const i7 = document.getElementById("i7");
        // Check if i7 is a positive number greater than 0
        if (i7.value > 0) {
            window.open(`/api/elev-metrics/limit/${i7.value}`, "_blank");
        } else {
            alert("Please enter a number greater than 0.");
        }
    }
}

function showPopUp() {popup = document.getElementById("popup");
popup.style.display = "block";}

function closePopUp() {popup = document.getElementById("popup");
popup.style.display = "none";}