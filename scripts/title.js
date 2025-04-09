window.addEventListener("load", function () {
    var pageTitle = document.title;
    var attentionMessage = "#alwaysquality";

    document.addEventListener("visibilitychange", function () {
        if (document.hidden) {
            document.title = attentionMessage;
        } else {
            document.title = pageTitle;
        }
    });
});
