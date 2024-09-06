import React from 'react';

const InterviewJoinButton = ({ interviewStatus, onJoin }) => {
  const buttonStyles = `inline-flex items-center justify-center px-6 py-2 rounded-md border border-transparent text-base font-medium shadow-sm text-white bg-[#4CAF50] hover:bg-[#45A049] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#4CAF50] transition duration-300 ease-in-out`;

  const handleJoinClick = () => {
    if (interviewStatus === 'scheduled') {
      onJoin();
    }
  };

  return (
    <button
      className={buttonStyles}
      onClick={handleJoinClick}
      disabled={interviewStatus !== 'scheduled'}
      style={{
        backgroundColor: interviewStatus === 'scheduled' ? '#4CAF50' : '#E0E0E0',
        cursor: interviewStatus === 'scheduled' ? 'pointer' : 'not-allowed',
      }}
    >
      {interviewStatus === 'scheduled' ? 'Join Interview' : 'Interview Not Scheduled'}
    </button>
  );
};

export default InterviewJoinButton;