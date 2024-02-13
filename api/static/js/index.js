function visitAPI(linkval) {
    if (linkval === 'link1'){
        const i1 = document.getElementById("i1");
        if (i1.value.slice(0,2) === "AT") {window.open(`/api/activities/activity-type/${i1.value}`, "_blank")};
    }
    else if (linkval === 'link2') {
        const i2 = document.getElementById("i2");
        if (i2.value > 0) {window.open(`/api/activities/limit/${i2.value}`, "_blank")};
    }
    else if (linkval === 'link3') {
        const i3a = document.getElementById("i3a");
        const i3b = document.getElementById("i3b");
        if ((i3a.value.at(4) === "-") && (i3a.value.at(7) === "-") && (i3b.value.at(4) === "-") && (i3b.value.at(7) === "-")) {window.open(`/api/activities/date/${i3a.value}/${i3b.value}`, "_blank")};
    }
    else if (linkval === 'link4') {
        const i4 = document.getElementById("i4");
        if (i4.value.slice(0,2) === "AT") {window.open(`/api/performance-metrics/activity-type/${i4.value}`, "_blank")};
    }
    else if (linkval === 'link5') {
        const i5 = document.getElementById("i5");
        if (i5.value > 0) {window.open(`/api/performance-metrics/limit/${i5.value}`, "_blank")};
    }
    else if (linkval === 'link6') {
        const i6 = document.getElementById("i6");
        if (i6.value > 0) {window.open(`/api/lap-metrics/limit/${i6.value}`, "_blank")};
    }
    else if (linkval === 'link7') {
        const i7 = document.getElementById("i7");
        if (i7.value > 0) {window.open(`/api/elev-metrics/limit/${i7.value}`, "_blank")};
    }
}

function showPopUp() {popup = document.getElementById("popup");
popup.style.display = "block";}

function closePopUp() {popup = document.getElementById("popup");
popup.style.display = "none";}