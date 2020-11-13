import React, {useContext} from 'react';
import { Navbar, Nav, Dropdown, ButtonGroup }from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faChartBar } from '@fortawesome/free-solid-svg-icons';
import {Link} from 'react-router-dom';
import {AuthContext} from './AuthContext';

const dropdownStyle = {backgroundColor:"#343a40"}

function Header() {
    const [state, setState] = useContext(AuthContext);

    const UserNameDropDown= (props) => {
        return (
            <Dropdown >
                <Dropdown.Toggle variant="dark" id="dropdown-basic">
                    {props.username}
                </Dropdown.Toggle>
            
                <Dropdown.Menu className="dropdown-menu-lg-right" style={dropdownStyle}>
                    <Dropdown.Item style={dropdownStyle}>My Teams</Dropdown.Item>
                    <Dropdown.Item style={dropdownStyle}>Logout</Dropdown.Item>
                </Dropdown.Menu>
            </Dropdown>
        );
    }

    let username;
    username = state.name ? <UserNameDropDown username={state.name}/> :  <Link to="/login" onClick={() => setState(state =>({...state, name:'Sammy'}))}>Login</Link>

    return (
        <Navbar sticky="top" bg="dark" variant="dark">
            <Navbar.Brand as={Link} to="/">
                Sport Stat Tracker {' '}
                <FontAwesomeIcon icon={faChartBar}/>
            </Navbar.Brand>
            <Nav className="mr-auto">
                <Nav.Link as={Link} exact to="/teams">Teams</Nav.Link>
                <Nav.Link as={Link} to="/players">Players</Nav.Link>
            </Nav>
            <Navbar.Collapse className="justify-content-end">
                <Navbar.Text>
                   {username}
                </Navbar.Text>
            </Navbar.Collapse>
        </Navbar> 
    )
}

export default Header
