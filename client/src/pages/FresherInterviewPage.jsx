import React from 'react';
import InterviewJoinButton from '../components/InterviewJoinButton';

const FresherInterviewPage = () => {
    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-white font-['Roboto']">
            <h1 className="text-2xl font-bold text-gray-800 mb-6" style={{ lineHeight: '1.5' }}>
                Welcome to the Fresher Interview Hub
            </h1>
            <p className="text-sm text-gray-600 mb-8" style={{ lineHeight: '1.6' }}>
                This interactive page serves as the central hub for freshers to access their interview sessions. It features the 
                <span className="font-semibold text-green-600"> 'InterviewJoinButton' </span>
                prominently, ensuring that users can easily locate and engage with it to join their interviews.
            </p>
            <InterviewJoinButton />
        </div>
    );
};

export default FresherInterviewPage;