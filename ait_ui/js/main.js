this.genRandomNumbers = () => {
    const array = new Uint32Array(10);
    crypto.getRandomValues(array);
    return Array.from(array).map(n => n.toString(16)).join('');
};

document.cookie = `locale=${localStorage.getItem('locale') || navigator.language || navigator.userLanguage}; path=/`;

class AlertHandler {
    constructor(element) {
        this.element = document.getElementById(element);
    }

    removeClass(className) {
        this.element.classList.remove(className);
    }

    addClass(className) {
        this.element.classList.add(className);
    }

    close(id, value) {
        this.removeClass('alert-start');
        this.addClass('alert-end');
    }

    open(type, message) {
        ['alert-normal', 'alert-success', 'alert-info', 'alert-warning', 'alert-danger']
            .forEach(cls => this.removeClass(cls));

        this.addClass(type);

        this.element.textContent = message;

        this.removeClass('alert-end');
        this.removeClass('alert-start');

        setTimeout(() => {
            this.addClass('alert-start');
        }, 100);
    }
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

const COOKIE_ATTRIBUTES = ['maxAge', 'path', 'httponly', 'secure', 'samesite'];

const clientPublicData = {
    locale: localStorage.getItem('locale') ? localStorage.getItem('locale') : navigator.language || navigator.userLanguage,
    userAgent: navigator.userAgent,
};

let socket;
let elements = {};
let event_handlers = {};

// Utility functions
const setCookie = (data) => {
    const value = data.value;
    let cookieString = `${value.name}=${value.value};`;
    COOKIE_ATTRIBUTES.forEach(attr => {
        if (value[attr]) {
            cookieString += attr === 'maxAge' ? `max-age=${value[attr]};` : `${attr}=${value[attr]};`;
        }
    });
    document.cookie = cookieString;
};

// Socket event handlers
const socketEvents = {
    'download-pdf': (data) => { generateCertificatePDF(data); },
    'set-cookie': setCookie,
    'delete-cookie': (data) => { document.cookie = `${data.value.name}=; max-age=0`; },
    'navigate': (data) => { window.location = data.value; },
    'scroll-to': (data) => { document.getElementById(data.id).scrollIntoView({ behavior: "smooth", block: "center", inline: "nearest" }); },
    'alert': (data) => { alert(data.value); },
    'focus': (data) => { document.getElementById(data.id).focus(); },
    'init-content': (data) => { document.getElementById(data.id).outerHTML = data.value; },
    'toggle-class': (data) => { document.getElementById(data.id).classList.toggle(data.value); },
    'add-class': (data) => { document.getElementById(data.id).classList.add(data.value); },
    'remove-class': (data) => { document.getElementById(data.id).classList.remove(data.value); },
};

async function clientEmit(id, newValue, event_name) {
    if (newValue instanceof File) {
        if (newValue.size > 100 * 1024 * 1024) {
            alert("File size exceeds the limit.");
            return;
        }
        return await uploadFile(newValue, id);
    }
    socket.emit('from_client', { id: id, value: newValue, event_name: event_name });
}

async function uploadFile(newValue, id) {
    const uid = genRandomNumbers();
    const formData = new FormData();
    formData.append("file", newValue);
    formData.append("id", id);
    formData.append("uid", uid);

    // FOR PYTHON USAGE MAKE CALL TO /file-upload
    //url to call = /file-upload

    return fetch("/api/images/", {
        method: "POST",
        body: formData,
        credentials: "include",
    })
        .then(async (response) => {
            if (!response.ok) {
                let error = await response.json();
                throw new Error(error.message ? error.message : response.statusText);
            }
            return response.json();
        })
        .then((data) => {
            socket.emit('from_client', { id: id, value: { uid: uid, file_name: newValue.name, data }, event_name: 'file-upload-started' });
        })
        .catch((error) => {
            if (window.comp_alert) {
                const inputElement = document.getElementById(id);
                if (inputElement) {
                    inputElement.value = '';
                }
                window.comp_alert.open('alert-danger', error.message);
                return;
            }
            alert(error.message);
        });
}

async function generateCertificatePDF(data) {
    const doc = new jspdf.jsPDF('p', 'pt', 'a4', true);

    doc.setProperties({
        title: 'Certificate',
        author: 'Your Name',
        subject: 'Certificate of Completion',
        keywords: 'Certificate, PDF',
    });

    doc.addFont('Exo2.ttf', 'Exo2', 'normal');
    doc.setFont('Exo2');

    const imgSrc = 'certificate_background.png';

    const pageWidth = doc.internal.pageSize.width;
    const pageHeight = doc.internal.pageSize.height;
    doc.addImage(imgSrc, 'JPEG', 0, 0, pageWidth, pageHeight, '', 'FAST');

    doc.setFontSize(20);
    doc.setTextColor(255, 255, 255);
    doc.text('Certificated By', 170, 300);
    doc.setFontSize(14);

    const logoSrc = 'AIT_White.png';
    const logoWidth = 100;
    const logoHeight = 50;
    const logoX = 220 + doc.getTextWidth('Certificated By');
    const logoY = 270;
    doc.addImage(logoSrc, 'JPEG', logoX, logoY, logoWidth, logoHeight);

    doc.text(`Certificate Belongs To : ${data.value.user.name}`, 200, 350);

    const imgWidth = data.value.dimensions.width;
    const imgHeight = data.value.dimensions.height;

    const maxHeight = 170;

    let newWidth, newHeight, xCoordinate;

    if (imgHeight > maxHeight) {
        const heightRatio = maxHeight / imgHeight;
        newHeight = maxHeight;
        newWidth = imgWidth * heightRatio;
        xCoordinate = (doc.internal.pageSize.getWidth() - newWidth / 2) / 2;
    } else {
        newWidth = imgWidth;
        newHeight = imgHeight;
        xCoordinate = (doc.internal.pageSize.getWidth() - newWidth / 2) / 2;
    }

    const yCoordinate = 370;

    doc.addImage(data.value.from_url, 'JPEG', xCoordinate, yCoordinate, 0, newHeight, '', 'FAST');

    doc.setFontSize(18);
    doc.text('CERTIFICATE OF AUTHENTICITY ', 130, pageHeight - 270);
    doc.setFontSize(12);
    doc.text('This is to certify that the pattern presented herein has been ', 130, pageHeight - 230);
    doc.text('generated by a state-of-the-art Artificial Intelligence (AI) system.', 130, pageHeight - 210);
    doc.text('The AI model employed for this purpose is a product of cutting-edge ', 130, pageHeight - 190);
    doc.text('technology and creative algorithms.  ', 130, pageHeight - 170);

    doc.setFontSize(12);
    doc.text(`Creation Date : ${data.value.createdOn}`, 200, pageHeight - 70);

    doc.save('certificate.pdf');
}



// NEW VERSION
const getSocketInstance = () => {
    if (!socket) {
        socket = io.connect(`${window.location.origin}`, {
            query: {
                clientPublicData: JSON.stringify(clientPublicData),
                session_id: getCookie('session_id'),
            },
            reconnection: true,
            reconnectionAttempts: 5,
            reconnectionDelay: 5000,
            transports: ['websocket']
        });
    }
    return socket;
};

const handleDynamicEvents = (data) => {
    if (data.event_name.startsWith("change-")) {
        if (data.event_name.split("-")[1] === "location") {
            window.location = data.value;
            return true;
        }
        const el = document.getElementById(data.id);
        el[data.event_name.split("-")[1]] = data.value;
        return true;
    }
    if (data.event_name.startsWith("set-")) {
        const el = document.getElementById(data.id);
        el['style'][data.event_name.split("-")[1]] = data.value;
        return true;
    }
    return false;
};

const initSocketEvents = () => {
    socket = getSocketInstance();

    if (socket.disconnected) {
        socket.connect();
    }

    socket.on('connect', () => {
        clientEmit('myapp', 'init', 'init');
    });

    socket.on('disconnect', () => { });

    socket.on('from_server', (data) => {
        if (socketEvents[data.event_name]) {
            socketEvents[data.event_name](data);
        } else if (handleDynamicEvents(data)) {
            return;
        } else if (event_handlers[data.event_name]) {
            event_handlers[data.event_name](data.id, data.value, data.event_name);
        }
    });

    socket.on('error', (error) => { });
};


const detachSocketEvents = () => {
    socket = getSocketInstance();
    socket.off('connect');
    socket.off('disconnect');
    socket.off('from_server');
    socket.disconnect();
    socket.close();
    socket = null;
};


window.addEventListener('load', initSocketEvents);

window.addEventListener('beforeunload', detachSocketEvents);