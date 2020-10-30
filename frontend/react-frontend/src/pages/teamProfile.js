import React, { useEffect, useState } from 'react';
import Header from "../Components/header";
import { useParams } from "react-router-dom";

const TeamProfile = ({ match }) => {
    const {
        params: { teamId },
    } = match

    return (
        <div className="container p-2">
        <Header/>
        <div>{teamId}</div>
        </div>
    );
};

export default TeamProfile;