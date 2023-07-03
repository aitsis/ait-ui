from components.element import Element
import components.scripts as scripts
import connection
scripts.header_items.append("<script src='https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.9.3/dropzone.min.js'></script>")

scripts.add_script("dropzone", """
    event_handlers["init-dropzone"] = function(id, value, event_name){            
        dropzone = document.getElementById(id);                
        var myDropzone = new Dropzone(dropzone, {
        paramName: "file",
        maxFilesize: 40, // MB
        maxFiles: 1,
        addRemoveLinks: true,
        uploadMultiple: false,
        acceptedFiles: "image/*",
        thumbnailWidth: 208,
        thumbnailHeight: 208,
        thumbnailMethod: "contain",
        url: "/file-management/files/upload",
        removedfile: function (file) {
            var _ref;
            return (_ref = file.previewElement) != null ? _ref.parentNode.removeChild(file.previewElement) : void 0;
        },
        init: function () {
            this.on("complete", function (file) {
                oldFile = file;
                return oldFile;
            });
            this.on("error", function (file, response) {
                return $(file.previewElement).find(".dz-error-message").text(response.message);
            });
            this.on("success", function (file, resp) {
                if (resp.length > 0) {
                    images = resp;
                    totalPages = 1;
                    doc.getElementById("currentPage").value = 1;
                    doc.getElementById("totalPages").innerHTML = totalPages;

                    return setMainLayout(searchView, currentLayout, true);
                } else return alert("No files found");
            });
            this.on("addedfile", function (file) {
                if (this.files.length > 1) this.removeFile(this.files[0]);
            });
            this.on("removedfile", function () {
            });
            this.on("sending", function (file, xhr, formData) {
                let searchType = doc.getElementById("searchType") ? doc.getElementById("searchType").value : "0";
                formData.append("searchType", searchType);
            });
        }
    });
    }
    """)

class File(Element):
    def __init__(self,id = None,value = None):
        super().__init__(id = id, value = value)                
        self.tag = "div"
        self.value_name = "value"
        self.has_content = False
    
    def render(self):
        if self.id is not None:            
            connection.queue_for_send(self.id, self.value, "init-dropzone")
        return super().render()