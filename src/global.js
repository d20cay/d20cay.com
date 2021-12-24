export const prodUrlRegex = /https?:\/\/d20cay\.com(?:\/[A-Za-z0-9_]+)*/
export const devUrlRegex = /https?:\/\/localhost:3000(?:\/[A-Za-z0-9_]+)*/


export function downloadableFileName(lead, sourceProgram, date) {
    const year = formatDatePart(date.getFullYear());
    const month = formatDatePart((date.getMonth() + 1));
    const day = formatDatePart(date.getDate());
    const hours = formatDatePart(date.getHours());
    const minutes = formatDatePart(date.getMinutes());
    const seconds = formatDatePart(date.getSeconds());
    return `${lead}${lead === "" ?
        "" :
        "_"}${sourceProgram}_${year}-${month}-${day}_${hours}-${minutes}-${seconds}.json`;
}

function formatDatePart(num) {
    const numString = num.toString();
    return numString.length > 1 ? numString : "0" + numString;
}


export const NotificationStatus = {
    NONE: '',
    PRIMARY: 'primary',
    SUCCESS: 'success',
    WARNING: 'warning',
    DANGER: 'danger'
};

export const NotificationPosition = {
    TOP_LEFT: 'top-left',
    TOP_CENTER: 'top-center',
    TOP_RIGHT: 'top-right',
    BOTTOM_LEFT: 'bottom-left',
    BOTTOM_CENTER: 'bottom-center',
    BOTTOM_RIGHT: 'bottom-right'
};

export const NotificationTimeout = {
    FLASH: 500,
    QUICK: 1000,
    MEDIUM: 3000,
    SLOW: 5000,
    CRITICAL: 10000,
    _CONTACT: 5 * 60 * 1000
};

export function notify(message, status, pos, timeout) {
    UIkit.notification({
        message: message,
        status: status,
        pos: pos,
        timeout: timeout
    });
}

export const LoadingStatus = {
    LOADING: 0,
    IDLE: 1,
    FAILED: 2
};

export function overwriteClipboard(string) {
    const el = document.createElement('textarea');
    el.setAttribute("class", "copy-text-holder");
    el.value = string;

    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);

    notify(`Copied "${string}" to clipboard.`,
        NotificationStatus.SUCCESS,
        NotificationPosition.BOTTOM_LEFT,
        NotificationTimeout.FLASH);
}

/**
 * Updates url parameters silently.
 *
 * @param    {string[][]}    parameters    Parameter values to update
 */
export function updateUrl(parameters) {
    const protocol = window.location.protocol;
    const host = window.location.host;
    const pathname = window.location.pathname;

    const params = new URLSearchParams(parameters);

    const newUrl = `${protocol}//${host}${pathname}${parameters.length === 0 ?
        '' :
        '?'}${params.toString()}`;
    window.history.replaceState({}, '', newUrl);
}

export function isProdInstance() {
    return prodUrlRegex.test(window.location.href);
}