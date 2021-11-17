// https://ralzohairi.medium.com/displaying-dynamic-elapsed-time-in-javascript-260fa0e95049
export function getElapsedTime(startTime) {
  let endTime = new Date();
  let timeDiff = endTime.getTime() - startTime.getTime();
  // Convert time difference from milliseconds to seconds
  timeDiff = timeDiff / 1000;
  // Extract integer seconds that do not form a minute using %
  let seconds = Math.floor(timeDiff % 60);
  // Convert time difference from seconds to minutes using %
  timeDiff = Math.floor(timeDiff / 60);
  // Extract integer minutes that don't form an hour using %
  let minutes = timeDiff % 60;
  // Convert time difference from minutes to hours
  timeDiff = Math.floor(timeDiff / 60);
  // Extract integer hours that don't form a day using %
  let hours = timeDiff % 24;
  // Convert time difference from hours to days
  timeDiff = Math.floor(timeDiff / 24);
  let days = timeDiff;
  // add days to hours
  let totalHours = hours + days * 24;
  if (totalHours === 0) {
    if (minutes === 0) {
      return `${seconds}s`;
    } else {
      return `${minutes}m`;
    }
  } else {
    return `${totalHours}h`;
  }
}
