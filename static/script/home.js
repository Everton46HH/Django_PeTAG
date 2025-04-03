let x = 0
function showSideContent(){
    if(document.getElementById("side-content").style.display == 'none'){
        document.getElementById("side-content").style.display = 'block'

    } else{
        document.getElementById("side-content").style.display = 'none'
    }
}

function KeyFrameLoad() {
    window.addEventListener("load", function() {
        setTimeout(function() {
            const container = document.getElementById("container-keyframe");
            container.style.opacity = '0';
            setTimeout(function() {
                container.style.display = 'none';
            }, 1000);
        }, 1000);
    });
}


KeyFrameLoad();