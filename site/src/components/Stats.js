import './Stats.scss';
import stats1 from '../temps/svg/stats1.svg'
import stats2 from '../temps/svg/stats2.svg'
import stats3 from '../temps/svg/stats3.svg'

function Stats(){
    return(
        <div className='Stats'>
            <div className='cont'>
                <div className='item'>
                    <img src={stats1} alt=''/>
                    <div className='text-item'>
                        <p className='c-gray fs-6'>Клиенты</p>
                        <h3>5,423</h3>
                        <p><span className='c-green fw-bold'>+16%</span> за этот месяц</p>
                    </div>
                </div>
                <span className='line'></span>
                <div className='item'>
                    <img src={stats2} alt=''/>
                    <div className='text-item'>
                        <p className='c-gray fs-6'>Ушло клиентов</p>
                        <h3>2</h3>
                        <p><span className='c-red fw-bold'>-1%</span> за этот месяц</p>
                    </div>
                </div>
                <span className='line'></span>
                <div className='item'>
                    <img src={stats3} alt=''/>
                    <div className='text-item'>
                        <p className='c-gray fs-6'>Прибыль</p>
                        <h3>20 млн. руб</h3>
                        <p><span className='c-green fw-bold'>+10%</span> за этот месяц</p>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Stats;