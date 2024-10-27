import './NavBar.scss'
import arrowRightW from '../temps/svg/arrot-right-white.svg'
import arrowRightG from '../temps/svg/arrot-right-grey.svg'
import user from '../temps/svg/user-square.svg'
import square from '../temps/svg/3d-square.svg'


function NavBar(){
    return(
        <div className="NavBar">
            <div className="Logo">
                <p>РЖД Таблица</p>
            </div>

            <div className="navigate">
                <div className="navLink active">
                    <div className='d-flex left'>
                        <img src={user} alt=""/>
                        <p className='fs-6'>
                            Клиентская база
                        </p>
                    </div>
                    
                    <img src={arrowRightW} alt="" className='arrow'/>
                </div>

                <div className="navLink">
                    <div className='d-flex left'>
                        <img src={square} alt=""/>
                        <p className='fs-6'>
                            Заявки
                        </p>
                    </div>
                    <img src={arrowRightG} alt="" className='arrow'/>
                </div>
            </div>
        </div>
    )
}

export default NavBar;