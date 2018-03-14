using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
 
namespace YourNamespace.Controllers
{
    public class HelloController : Controller
    {
        [HttpGet]
        [Route("")]
        public string DisplayOptions()
        {
            return "Use the following URL options for the app, /firstname, /lastname, /age, /favcolor. Each will return my info.";
        }
        
        [HttpGet]
        [Route("firstname")]
        public JsonResult DisplayFirstName()
        {
            return Json("Rick");
        }
        [Route("lastname")]
        public JsonResult DisplayLastName()
        {
            return Json("Sanchez");
        }
        [Route("age")]
        public JsonResult DisplayAge()
        {
            return Json("64");
        }
        [Route("favcolor")]
        public JsonResult DisplayFavColor()
        {
            return Json("Red");
        }
        [HttpGet]
        [Route("{firstName}/{lastName}/{age}/{faveColor}")]
        public JsonResult Jsonify(string firstName, string lastName, int age, string faveColor)
        {
          var callCard = new {
            FirstName = firstName,
            LastName = lastName,
            Age = age,
            FaveColor = faveColor
          };
          return Json(callCard);
        }
        [HttpGet]
        [Route("bonus")]
        public IActionResult Index()
        {
            return View();
        }
    }
       
}