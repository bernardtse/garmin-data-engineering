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
            alert("Please enter 